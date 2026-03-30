"""
Crawl the Helmet Lab SharePoint and dump the file tree for cataloging.

Usage:
    uv run python sharepoint_crawl.py

Auth: Device code flow — the script prints a URL + code, you sign in via browser.
"""

import json
import sys
import time
from pathlib import Path

import msal
import requests

# ── SharePoint target ─────────────────────────────────────────
SP_HOSTNAME = "virginiatech.sharepoint.com"
SP_SITE_PATH = "/sites/VirginiaTechHelmetLab-OlderAdultTBI"
ROOT_FOLDER = "Older Adult TBI"  # inside the default "Shared Documents" drive

# ── Auth config ───────────────────────────────────────────────
# "Microsoft Graph Command Line Tools" — a pre-registered multi-tenant
# public client that supports device-code flow.  Works in most M365 tenants.
# If your org blocks it, register your own app (see README) and paste the ID here.
CLIENT_ID = "14d82eec-204b-4c2f-b7e8-296a70dab67e"
AUTHORITY = "https://login.microsoftonline.com/organizations"
SCOPES = ["Sites.Read.All", "Files.Read.All"]

GRAPH = "https://graph.microsoft.com/v1.0"
OUTPUT_FILE = Path(__file__).parent / "sharepoint_tree.json"
TOKEN_CACHE_FILE = Path(__file__).parent / ".token_cache.json"


# ── Auth ──────────────────────────────────────────────────────
def _load_cache() -> msal.SerializableTokenCache:
    cache = msal.SerializableTokenCache()
    if TOKEN_CACHE_FILE.exists():
        cache.deserialize(TOKEN_CACHE_FILE.read_text())
    return cache


def _save_cache(cache: msal.SerializableTokenCache):
    if cache.has_state_changed:
        TOKEN_CACHE_FILE.write_text(cache.serialize())


def authenticate() -> str:
    """Try cached token first, fall back to device-code flow."""
    cache = _load_cache()
    app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

    # Try silent auth with cached refresh token
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result and "access_token" in result:
            _save_cache(cache)
            print(f"Using cached token for {accounts[0]['username']}")
            return result["access_token"]

    # Fall back to device code flow
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        print(f"Auth error: {json.dumps(flow, indent=2)}")
        sys.exit(1)

    print()
    print("=" * 60)
    print(f"  Go to:  {flow['verification_uri']}")
    print(f"  Enter:  {flow['user_code']}")
    print("=" * 60)
    print()
    print("Waiting for you to sign in...")

    result = app.acquire_token_by_device_flow(flow)
    _save_cache(cache)

    if "access_token" not in result:
        print(f"Auth failed: {result.get('error_description', result)}")
        sys.exit(1)

    print(f"Signed in as {result.get('id_token_claims', {}).get('preferred_username', '?')}")
    return result["access_token"]


# ── Graph helpers ─────────────────────────────────────────────
def graph_get(token: str, url: str, params: dict | None = None) -> dict:
    """GET from Graph API with automatic pagination."""
    headers = {"Authorization": f"Bearer {token}"}
    items = []

    while url:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 429:
            retry = int(resp.headers.get("Retry-After", 5))
            print(f"  Throttled, waiting {retry}s...")
            time.sleep(retry)
            continue
        resp.raise_for_status()
        data = resp.json()

        if "value" in data:
            items.extend(data["value"])
            url = data.get("@odata.nextLink")
            params = None  # nextLink includes params
        else:
            return data

    return {"value": items}


def resolve_site(token: str) -> str:
    """Get the site ID."""
    data = graph_get(token, f"{GRAPH}/sites/{SP_HOSTNAME}:{SP_SITE_PATH}")
    site_id = data["id"]
    print(f"Site: {data['displayName']} ({site_id})")
    return site_id


def get_default_drive(token: str, site_id: str) -> str:
    """Get the default document library drive ID."""
    data = graph_get(token, f"{GRAPH}/sites/{site_id}/drive")
    drive_id = data["id"]
    print(f"Drive: {data['name']} ({drive_id})")
    return drive_id


def crawl_folder(token: str, drive_id: str, folder_path: str, depth: int = 0) -> list[dict]:
    """Recursively crawl a folder and return file/folder metadata."""
    prefix = "  " * depth
    encoded_path = requests.utils.quote(folder_path)
    url = f"{GRAPH}/drives/{drive_id}/root:/{encoded_path}:/children"

    try:
        data = graph_get(token, url, params={"$top": "200"})
    except requests.HTTPError as e:
        print(f"{prefix}  ERROR crawling {folder_path}: {e}")
        return []

    results = []
    items = data.get("value", [])
    print(f"{prefix}/{folder_path.split('/')[-1]}  ({len(items)} items)")

    for item in items:
        entry = {
            "name": item["name"],
            "path": f"{folder_path}/{item['name']}",
            "size": item.get("size", 0),
            "created": item.get("createdDateTime"),
            "modified": item.get("lastModifiedDateTime"),
            "created_by": (
                item.get("createdBy", {}).get("user", {}).get("displayName")
            ),
            "web_url": item.get("webUrl"),
        }

        if "folder" in item:
            entry["type"] = "folder"
            entry["child_count"] = item["folder"]["childCount"]
            entry["children"] = crawl_folder(
                token, drive_id, entry["path"], depth + 1
            )
        else:
            entry["type"] = "file"
            ext = Path(item["name"]).suffix.lower()
            entry["extension"] = ext
            mime = item.get("file", {}).get("mimeType", "")
            entry["mime_type"] = mime

        results.append(entry)

    return results


# ── Summary ───────────────────────────────────────────────────
def summarize(tree: list[dict], stats: dict | None = None) -> dict:
    if stats is None:
        stats = {"files": 0, "folders": 0, "total_bytes": 0, "extensions": {}}

    for item in tree:
        if item["type"] == "folder":
            stats["folders"] += 1
            summarize(item.get("children", []), stats)
        else:
            stats["files"] += 1
            stats["total_bytes"] += item.get("size", 0)
            ext = item.get("extension", "?")
            stats["extensions"][ext] = stats["extensions"].get(ext, 0) + 1

    return stats


# ── Main ──────────────────────────────────────────────────────
def main():
    token = authenticate()

    print("\nResolving SharePoint site...")
    site_id = resolve_site(token)
    drive_id = get_default_drive(token, site_id)

    print(f"\nCrawling /{ROOT_FOLDER}/ ...")
    tree = crawl_folder(token, drive_id, ROOT_FOLDER)

    # Save full tree
    OUTPUT_FILE.write_text(json.dumps(tree, indent=2, default=str))
    print(f"\nTree saved to {OUTPUT_FILE}")

    # Print summary
    stats = summarize(tree)
    size_gb = stats["total_bytes"] / (1024**3)
    print(f"\n{'=' * 50}")
    print(f"  Files:   {stats['files']}")
    print(f"  Folders: {stats['folders']}")
    print(f"  Size:    {size_gb:.1f} GB")
    print(f"  Types:   {dict(sorted(stats['extensions'].items(), key=lambda x: -x[1]))}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
