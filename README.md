# Data Catalog

Centralized dataset registry for the Virginia Tech Helmet Lab. Tracks datasets, storage locations, annotations, lineage, and project usage across the lab's research projects.

## Overview

The catalog is a SQLite database (`catalog.db`) with an installable Python package for programmatic access and a Datasette web interface for browsing. It indexes datasets across the HPC cluster and SharePoint without duplicating the underlying data -- it stores metadata and pointers to where files live.

Currently tracks 36 datasets (~366GB) across 4 modalities (video, image, signal, point-cloud) and 3 research domains (fall detection, histotripsy, friendship study), with 25 lineage records tracking how datasets derive from each other.

## Installation

The catalog is a uv library with zero core dependencies. Other projects can add it as a path dependency:

```toml
# In another project's pyproject.toml
dependencies = [
    "data-catalog @ file:///projects/helmetlab1/Data-Catalog",
]
```

Optional extras:

```toml
"data-catalog[viewer] @ file:///projects/helmetlab1/Data-Catalog"     # Datasette web UI
"data-catalog[sharepoint] @ file:///projects/helmetlab1/Data-Catalog"  # SharePoint crawling
"data-catalog[all] @ file:///projects/helmetlab1/Data-Catalog"         # Everything
```

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

### Initialize the database

```bash
uv run python scripts/seed.py
```

This creates `catalog.db` and populates it with all 36 datasets, 46 storage locations, 7 annotation sets, 25 lineage records, 25 tags, and 7 project links. The seed is auto-generated from the canonical catalog state and is idempotent.

### Browse with Datasette

```bash
uv run datasette catalog.db \
    --metadata datasette_metadata.yml \
    --template-dir templates \
    --static static:static \
    --port 8001 --host 0.0.0.0
```

On the VT HPC cluster (OOD), the `data` shell alias runs this with the correct proxy base URL automatically.

## Programmatic Access

```python
from data_catalog.db import get_connection

conn = get_connection()
for row in conn.execute("SELECT name, modality, domain FROM datasets"):
    print(row["name"], row["modality"], row["domain"])
```

## Schema

Seven tables in `src/data_catalog/schema.sql`:

| Table | Purpose |
|---|---|
| `datasets` | Core registry. Name, modality, domain, description. |
| `dataset_stats` | Per-dataset summary: sample count, size, format, resolution, fps. |
| `storage_locations` | Where copies live. One dataset can have multiple locations (cluster, SharePoint, cloud). Primary flag marks the canonical copy. |
| `annotations` | Published annotation sets per dataset. Tracks type (temporal, bbox, keypoints, classification), format, path, and count. |
| `lineage` | Parent-child relationships between datasets. Tracks derivation method (augmented_from, subset_of, merged_from, reformatted_from). |
| `tags` / `dataset_tags` | Freeform labels for filtering (e.g., fall-detection, multi-camera, yolo11, pose-estimation). |
| `projects` / `project_datasets` | Which research projects use which datasets, in what role (train, eval, test, reference). |

## Scripts

| Script | Purpose |
|---|---|
| `scripts/seed.py` | Populate the catalog from scratch. Auto-generated from the canonical DB state. Idempotent. |
| `scripts/sharepoint_crawl.py` | Authenticate to the Helmet Lab SharePoint via MSAL device code flow and recursively crawl the file tree. Outputs `sharepoint_tree.json`. |
| `scripts/sharepoint_download.py` | Download datasets from SharePoint to the cluster using the crawled tree and cached auth token. Supports resume. |
| `scripts/harup_zip_to_video.sh` | Convert HAR-UP PNG image sequence ZIPs to H.264 MP4 videos at 15fps. |

## Data Directory

Ground truth dataset files live in `data/` (gitignored). Each dataset family has a parent folder containing raw data and any derived versions:

```
data/
├── robinovich/                 1.1GB   300 mp4 fall videos
│   ├── annotations/                    temporal fall annotations (JSON)
│   └── pose-yolo11/            4.1GB   YOLO11 keypoints + skeleton overlay videos
├── le2i/                       17GB    190 avi fall videos, 6 indoor scenes
│   ├── pose-yolo11/            1.5GB   YOLO11 keypoints + overlays + kinematics
│   ├── benchmark-5model/       4.3GB   5-model benchmark (YOLO11-L/XL, RTMPose, MediaPipe)
│   └── falldataset-imvia.zip   9.4GB   original Kaggle archive
├── ku-leuven/
│   ├── videos/                 4.3GB   270 avi multi-camera fall videos
│   └── pose-yolo11/            13GB    YOLO11 keypoints + skeleton videos
├── ur-fall/
│   ├── original/               116MB   100 side-by-side (depth+RGB) videos
│   ├── adl-rgb/                5MB     40 ADL sequences, RGB only
│   ├── adl-depth/              16MB    40 ADL sequences, depth/IR only
│   ├── falls-rgb/              195MB   60 fall sequences, RGB only
│   ├── falls-depth/            203MB   60 fall sequences, depth/IR only
│   └── rgb-pose-yolo11/        1.2GB   YOLO11 keypoints + skeleton videos (RGB)
├── sisfall/
│   ├── signals/                217MB   accelerometer/gyroscope data (ZIP + CSV)
│   ├── videos/                 26MB    34 demo videos from YouTube
│   └── pose-yolo11/            888MB   YOLO11 keypoints + skeleton videos
├── har-up/
│   ├── archives/               276GB   1,111 ZIP image sequence archives
│   ├── videos/                 1.3GB   1,111 stitched MP4s at 15fps
│   ├── falls/                          510 fall videos (symlinks, Activity 1-5)
│   ├── adl/                            601 ADL videos (symlinks, Activity 6-11)
│   └── falls-pose-yolo11/     3.0GB   YOLO11 keypoints + skeleton videos (falls only)
├── multiple-cameras-fall/
│   ├── dataset/                3.6GB   192 avi (24 scenes x 8 cameras)
│   └── pose-yolo11/            7.8GB   YOLO11 keypoints + skeleton videos
├── fall-signal/                12GB    accelerometer + geophone CSVs (3 sessions)
├── histotripsy/                3.2GB   DICOM CT scans + ultrasound video
├── friendship/
│   ├── room-videos/            6.3GB   27 Avigilon camera recordings
│   └── faro-scans/             3.9GB   FARO 3D room scans
└── set-elderly/
    └── SetElderly/             178MB   413 labeled PNGs (YOLO bbox format)
```

## Projects

The catalog tracks 7 research projects and their dataset usage:

| Project | Datasets Used | Role |
|---|---|---|
| Label-Software | (via catalog integration) | annotation |
| Pose-Detection | 8 pose estimation outputs | processing |
| Fall-Detector | robinovich, le2i | training |
| Fall-Signal | fall-signal | analysis |
| Histotripsy | histotripsy-ct, histotripsy-us | analysis |
| Impact-Locations | le2i-pose-yolo11 | training |
| Friendship-Study | friendship-room, friendship-faro | research |

## Integration with Label-Software

The catalog integrates with [Label-Software](https://github.com/Virginia-Tech-Helmet-Lab/fall-detection-data-handler) for video annotation. Label-Software imports `data_catalog` as a dependency to browse datasets and import videos by reference (no file copying). When annotations are finalized, they are published back to the catalog's `annotations` table with a versioned JSON export written to the dataset's directory.

## Integration with Pose-Detection

The [Pose-Detection](../Pose-Detection) library is also installable as a uv package. The catalog serves as the single source of truth for all pose estimation outputs -- raw videos are read from catalog paths, and keypoint/overlay outputs are stored back under each dataset's family directory.

## Project Structure

```
.
├── src/data_catalog/
│   ├── __init__.py         # Package root
│   ├── db.py               # get_connection(), init_db()
│   └── schema.sql          # Table definitions
├── scripts/
│   ├── seed.py             # Database seeding (auto-generated)
│   ├── sharepoint_crawl.py # SharePoint file tree discovery
│   ├── sharepoint_download.py  # SharePoint file download
│   └── harup_zip_to_video.sh   # HAR-UP ZIP-to-MP4 converter
├── templates/              # Datasette HTML templates (VT themed)
├── static/                 # Datasette CSS (VT brand colors)
├── datasette_metadata.yml  # Datasette config + canned queries
├── pyproject.toml          # uv library (zero core deps)
└── uv.lock
```
