"""
Download datasets from the Helmet Lab SharePoint to the cluster.

Uses the cached MSAL token from sharepoint_crawl.py and the file tree
from sharepoint_tree.json to download specific dataset folders.

Usage:
    uv run python sharepoint_download.py
"""

import json
import sys
import time
from pathlib import Path

import msal
import requests

# ── Config ────────────────────────────────────────────────────
CLIENT_ID = "14d82eec-204b-4c2f-b7e8-296a70dab67e"
AUTHORITY = "https://login.microsoftonline.com/organizations"
SCOPES = ["Sites.Read.All", "Files.Read.All"]
GRAPH = "https://graph.microsoft.com/v1.0"
DRIVE_ID = "b!wljQIg_pwECAOd39Z6Blhbmu4ao1S3tCtSMQUUk83T9hjIBG7L6cSrU5MuFfgUfL"

TOKEN_CACHE_FILE = Path(__file__).parent / ".token_cache.json"
TREE_FILE = Path(__file__).parent / "sharepoint_tree.json"
DATA_DIR = Path(__file__).parent / "data"
LOG_FILE = Path(__file__).parent / "download_log.json"

# Map SharePoint paths to local dataset folders.
# Keys are prefixes matched against item paths in sharepoint_tree.json.
# Value is the local subdirectory under DATA_DIR.
DOWNLOAD_MAP = {
    # Public fall sets (skip "Optimised spatio-temporal" = le2i duplicate, skip SDUFall = links only)
    "Data/Publically Avalible Fall Sets/Downloaded Data/Not Using HAR-UP Fall Dataset":
        "public-fall-sets/har-up",
    "Data/Publically Avalible Fall Sets/Downloaded Data/Ku Leuven RDR":
        "public-fall-sets/ku-leuven-rdr",
    "Data/Publically Avalible Fall Sets/Downloaded Data/UR Fall Detection Data Set":
        "public-fall-sets/ur-fall-detection",
    "Data/Publically Avalible Fall Sets/Downloaded Data/Not Using Multiple Cameras Fall Data Set":
        "public-fall-sets/multiple-cameras-fall",
    "Data/Publically Avalible Fall Sets/Downloaded Data/Sis Fall Dataset":
        "public-fall-sets/sisfall",
    "Data/Publically Avalible Fall Sets/setElderly.zip":
        "public-fall-sets",

    # Friendship datasets
    "Data/Friendship In Room":
        "friendship-room",
    "Friendship Information/FARO":
        "friendship-faro",
}


# ── Auth ──────────────────────────────────────────────────────
def authenticate() -> str:
    cache = msal.SerializableTokenCache()
    if TOKEN_CACHE_FILE.exists():
        cache.deserialize(TOKEN_CACHE_FILE.read_text())

    app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result and "access_token" in result:
            if cache.has_state_changed:
                TOKEN_CACHE_FILE.write_text(cache.serialize())
            print(f"Authenticated as {accounts[0]['username']}")
            return result["access_token"]

    # Fall back to device code
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        print(f"Auth error: {json.dumps(flow, indent=2)}")
        sys.exit(1)
    print(f"\n  Go to:  {flow['verification_uri']}\n  Enter:  {flow['user_code']}\n")
    result = app.acquire_token_by_device_flow(flow)
    if cache.has_state_changed:
        TOKEN_CACHE_FILE.write_text(cache.serialize())
    if "access_token" not in result:
        print(f"Auth failed: {result.get('error_description', result)}")
        sys.exit(1)
    return result["access_token"]


def refresh_token() -> str:
    """Get a fresh access token (handles silent refresh)."""
    return authenticate()


# ── Download helpers ──────────────────────────────────────────
def download_file(token: str, sp_path: str, local_path: Path, expected_size: int) -> bool:
    """Download a single file from SharePoint. Returns True on success."""
    # Resume: skip if file exists with correct size
    if local_path.exists() and local_path.stat().st_size == expected_size:
        return True

    local_path.parent.mkdir(parents=True, exist_ok=True)

    encoded = requests.utils.quote(sp_path)
    url = f"{GRAPH}/drives/{DRIVE_ID}/root:/{encoded}:/content"
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(3):
        try:
            resp = requests.get(url, headers=headers, stream=True, timeout=60, allow_redirects=True)

            if resp.status_code == 429:
                retry = int(resp.headers.get("Retry-After", 10))
                print(f"    Throttled, waiting {retry}s...")
                time.sleep(retry)
                continue

            if resp.status_code == 401:
                # Token expired, caller should refresh
                return False

            resp.raise_for_status()

            # Stream to disk in 1MB chunks
            tmp = local_path.with_suffix(local_path.suffix + ".tmp")
            downloaded = 0
            with open(tmp, "wb") as f:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    f.write(chunk)
                    downloaded += len(chunk)

            tmp.rename(local_path)
            return True

        except (requests.ConnectionError, requests.Timeout) as e:
            wait = 2 ** attempt * 5
            print(f"    Network error: {e}. Retrying in {wait}s...")
            time.sleep(wait)

    return False


def collect_files(tree: list[dict], prefix: str = "") -> list[dict]:
    """Flatten the tree into a list of files with their full paths."""
    files = []
    for item in tree:
        item_path = f"{prefix}/{item['name']}" if prefix else item["name"]
        # Reconstruct the full SharePoint path
        full_path = item.get("path", item_path)
        if item["type"] == "file":
            files.append({
                "path": full_path,
                "name": item["name"],
                "size": item.get("size", 0),
            })
        elif item["type"] == "folder":
            files.extend(collect_files(item.get("children", []), item_path))
    return files


def find_subtree(tree: list[dict], target_path: str) -> list[dict] | dict | None:
    """Find a subtree by path prefix."""
    parts = target_path.split("/")

    def _search(nodes, remaining_parts):
        if not remaining_parts:
            return nodes
        target = remaining_parts[0]
        for node in nodes:
            if node["name"] == target:
                if len(remaining_parts) == 1:
                    if node["type"] == "folder":
                        return node.get("children", [])
                    else:
                        return node  # single file
                else:
                    return _search(node.get("children", []), remaining_parts[1:])
        return None

    return _search(tree, parts)


# ── Main ──────────────────────────────────────────────────────
def main():
    if not TREE_FILE.exists():
        print("Run sharepoint_crawl.py first to generate sharepoint_tree.json")
        sys.exit(1)

    print("Loading SharePoint tree...")
    tree = json.loads(TREE_FILE.read_text())

    token = authenticate()

    # Build download manifest
    manifest = []  # list of (sp_path, local_path, size)
    for sp_prefix, local_subdir in DOWNLOAD_MAP.items():
        subtree = find_subtree(tree, sp_prefix)
        if subtree is None:
            print(f"  WARNING: path not found in tree: {sp_prefix}")
            continue

        if isinstance(subtree, dict):
            # Single file
            local_path = DATA_DIR / local_subdir / subtree["name"]
            manifest.append((subtree["path"], local_path, subtree.get("size", 0)))
        else:
            # Folder -- the last component of sp_prefix is the folder we descended into.
            # File paths in the tree are like "Older Adult TBI/Data/.../FolderName/subdir/file.ext".
            # We want the part AFTER the folder name.
            folder_name = sp_prefix.split("/")[-1]
            files = collect_files(subtree)
            for f in files:
                full = f["path"]
                # Find the folder name in the path and take everything after it
                marker = f"/{folder_name}/"
                idx = full.find(marker)
                if idx >= 0:
                    rel = full[idx + len(marker):]
                else:
                    rel = f["name"]

                local_path = DATA_DIR / local_subdir / rel
                manifest.append((full, local_path, f.get("size", 0)))

    total_files = len(manifest)
    total_bytes = sum(m[2] for m in manifest)
    print(f"\nDownload manifest: {total_files} files, {total_bytes / 1024**3:.1f} GB")

    # Check how many already exist
    existing = sum(1 for _, lp, sz in manifest if lp.exists() and lp.stat().st_size == sz)
    print(f"Already downloaded: {existing}/{total_files}")

    if existing == total_files:
        print("All files already downloaded!")
        save_log(manifest, [])
        return

    # Download
    failures = []
    downloaded_bytes = 0
    downloaded_count = 0
    skipped_count = existing

    for i, (sp_path, local_path, size) in enumerate(manifest, 1):
        if local_path.exists() and local_path.stat().st_size == size:
            continue  # already have it

        pct = (i / total_files) * 100
        size_mb = size / 1024**2
        print(f"  [{i}/{total_files} {pct:.0f}%] {local_path.name} ({size_mb:.1f} MB)")

        ok = download_file(token, sp_path, local_path, size)

        if not ok:
            # Try token refresh
            print("    Refreshing token...")
            token = refresh_token()
            ok = download_file(token, sp_path, local_path, size)

        if ok:
            downloaded_count += 1
            downloaded_bytes += size
        else:
            failures.append(sp_path)
            print(f"    FAILED: {sp_path}")

        # Progress summary every 50 files
        if downloaded_count > 0 and downloaded_count % 50 == 0:
            print(f"  --- Progress: {downloaded_count} downloaded, "
                  f"{downloaded_bytes / 1024**3:.1f} GB, "
                  f"{len(failures)} failures ---")

    print(f"\nDone! Downloaded {downloaded_count} files ({downloaded_bytes / 1024**3:.1f} GB)")
    if failures:
        print(f"  {len(failures)} failures")
    save_log(manifest, failures)


def save_log(manifest, failures):
    log = {
        "total_files": len(manifest),
        "total_bytes": sum(m[2] for m in manifest),
        "failures": failures,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    LOG_FILE.write_text(json.dumps(log, indent=2))
    print(f"Log saved to {LOG_FILE}")


if __name__ == "__main__":
    main()
