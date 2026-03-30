# Data Catalog

Centralized dataset registry for the Virginia Tech Helmet Lab. Tracks datasets, storage locations, annotations, lineage, and project usage across the lab's research projects.

## Overview

The catalog is a SQLite database (`catalog.db`) with a Python package for programmatic access and a Datasette web interface for browsing. It indexes datasets across the HPC cluster and SharePoint without duplicating the underlying data -- it stores metadata and pointers to where files live.

Currently tracks 13 datasets (~327GB) across 3 modalities (video, image/DICOM, signal) and 3 research domains (fall detection, histotripsy, friendship study).

## Schema

Seven tables in `src/data_catalog/schema.sql`:

| Table | Purpose |
|---|---|
| `datasets` | Core registry. Name, modality, domain, description. |
| `dataset_stats` | Per-dataset summary: sample count, size, format, resolution, fps. |
| `storage_locations` | Where copies live. One dataset can have multiple locations (cluster, SharePoint, cloud). Primary flag marks the canonical copy. |
| `annotations` | Published annotation sets per dataset. Tracks type (temporal, bbox, keypoints), format (json, txt, csv), path, and count. |
| `lineage` | Parent-child relationships between datasets. Tracks derivation method (augmented_from, subset_of, merged_from, reformatted_from). |
| `tags` / `dataset_tags` | Freeform labels for filtering (e.g., fall-detection, multi-camera, yolo11). |
| `projects` / `project_datasets` | Which research projects use which datasets, in what role (train, eval, test, reference). |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

### Initialize the database

```bash
uv run python scripts/seed.py
```

This creates `catalog.db` and populates it with all known datasets, storage locations, annotations, tags, and project links.

### Browse with Datasette

```bash
uv run datasette catalog.db \
    --metadata datasette_metadata.yml \
    --template-dir templates \
    --static static:static \
    --port 8001 --host 0.0.0.0
```

On the VT HPC cluster (OOD), append the base URL for proxy routing:

```bash
uv run datasette catalog.db \
    --metadata datasette_metadata.yml \
    --template-dir templates \
    --static static:static \
    --port 8001 --host 0.0.0.0 \
    --setting base_url /rnode/$HOSTNAME/$port/proxy/8001/
```

The `data` shell alias (defined in `~/.bashrc`) runs this automatically.

## Programmatic Access

```python
from src.data_catalog.db import get_connection

conn = get_connection()
for row in conn.execute("SELECT name, modality, domain FROM datasets"):
    print(row["name"], row["modality"], row["domain"])
```

## Scripts

| Script | Purpose |
|---|---|
| `scripts/seed.py` | Populate the catalog with all known datasets. Idempotent (uses INSERT OR IGNORE). |
| `scripts/sharepoint_crawl.py` | Authenticate to the Helmet Lab SharePoint via MSAL device code flow and recursively crawl the file tree. Outputs `sharepoint_tree.json`. |
| `scripts/sharepoint_download.py` | Download datasets from SharePoint to the cluster using the crawled tree and cached auth token. Supports resume (skips files that already exist with matching size). |

## Data Directory

Ground truth dataset files live in `data/` (gitignored). Structure:

```
data/
├── robinovich/                 1.1GB   300 mp4 fall videos
├── robinovich-pose-yolo11/     4.1GB   YOLO11 keypoints + skeleton videos
├── le2i/                       17GB    190 avi fall videos, 6 scenes
├── fall-signal/                12GB    accelerometer + geophone CSVs
├── histotripsy/                3.2GB   DICOM CT + ultrasound video
├── public-fall-sets/           284GB   HAR-UP, Ku Leuven, UR Fall, etc.
├── friendship-room/            6.3GB   Avigilon camera recordings
└── friendship-faro/            3.9GB   FARO 3D room scans
```

## Integration with Label-Software

The catalog integrates with [Label-Software](https://github.com/Virginia-Tech-Helmet-Lab/fall-detection-data-handler) for video annotation. Label-Software reads `catalog.db` to browse datasets and import videos by reference (no file copying). When annotations are finalized, they are published back to the catalog's `annotations` table with a versioned JSON export written to the dataset's directory.

## Project Structure

```
.
├── src/data_catalog/
│   ├── db.py               # get_connection(), init_db()
│   └── schema.sql          # Table definitions
├── scripts/
│   ├── seed.py             # Database seeding
│   ├── sharepoint_crawl.py # SharePoint file tree discovery
│   └── sharepoint_download.py  # SharePoint file download
├── templates/              # Datasette HTML templates (VT themed)
├── static/                 # Datasette CSS (VT brand colors)
├── datasette_metadata.yml  # Datasette config + canned queries
├── pyproject.toml
└── uv.lock
```
