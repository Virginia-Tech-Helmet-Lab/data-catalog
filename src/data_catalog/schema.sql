-- Data Catalog Schema
-- Designed for the VT Helmet Lab's mixed-modality research datasets

PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-----------------------------------------------------------
-- DATASETS: the core entity. A logical collection of data.
-----------------------------------------------------------
CREATE TABLE IF NOT EXISTS datasets (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL UNIQUE,        -- e.g. "robinovich", "le2i"
    description     TEXT,
    modality        TEXT NOT NULL,               -- video | image | signal
    domain          TEXT,                        -- e.g. "fall-detection", "pose-estimation"
    source_url      TEXT,                        -- original download / paper link
    license         TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-----------------------------------------------------------
-- DATASET_STATS: summary-level numbers for a dataset.
-----------------------------------------------------------
CREATE TABLE IF NOT EXISTS dataset_stats (
    dataset_id      INTEGER PRIMARY KEY REFERENCES datasets(id),
    num_samples     INTEGER,                    -- total files (videos, images, etc.)
    total_size_bytes INTEGER,
    format          TEXT,                        -- dominant format: mp4, avi, png, npy ...
    resolution      TEXT,                        -- e.g. "640x480" or "mixed"
    fps             REAL,                        -- null if not video
    duration_sec    REAL                         -- total duration, null if not video
);

-----------------------------------------------------------
-- STORAGE_LOCATIONS: where a dataset (or copy) physically lives.
-- One dataset can exist in multiple places.
-----------------------------------------------------------
CREATE TABLE IF NOT EXISTS storage_locations (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset_id      INTEGER NOT NULL REFERENCES datasets(id),
    location_type   TEXT NOT NULL,               -- cluster | sharepoint | external
    path            TEXT NOT NULL,               -- filesystem path or URL
    is_primary      INTEGER NOT NULL DEFAULT 0,  -- 1 = canonical copy
    size_bytes      INTEGER,
    verified_at     TEXT,                         -- last time we confirmed it exists
    notes           TEXT,
    UNIQUE(dataset_id, path)
);

-----------------------------------------------------------
-- ANNOTATIONS: annotation sets that go with a dataset.
-- A dataset can have multiple annotation sets (different labelers, formats, tasks).
-----------------------------------------------------------
CREATE TABLE IF NOT EXISTS annotations (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset_id      INTEGER NOT NULL REFERENCES datasets(id),
    name            TEXT NOT NULL,               -- e.g. "temporal_falls", "bbox_per_frame"
    annotation_type TEXT NOT NULL,               -- temporal | bbox | segmentation | keypoints | classification
    format          TEXT NOT NULL,               -- json | txt | csv | xml | coco
    path            TEXT,                        -- where the annotation files live
    num_annotations INTEGER,
    created_by      TEXT,                        -- person or tool that made them
    notes           TEXT,
    UNIQUE(dataset_id, name)
);

-----------------------------------------------------------
-- LINEAGE: tracks how datasets relate to each other.
-- e.g. "le2i_augmented" was derived from "le2i" via "horizontal_flip + color_jitter"
-----------------------------------------------------------
CREATE TABLE IF NOT EXISTS lineage (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id       INTEGER NOT NULL REFERENCES datasets(id),
    child_id        INTEGER NOT NULL REFERENCES datasets(id),
    relationship    TEXT NOT NULL,               -- augmented_from | subset_of | merged_from | reformatted_from
    transform       TEXT,                        -- description of what was done
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE(parent_id, child_id, relationship)
);

-----------------------------------------------------------
-- TAGS: freeform labels for filtering.
-----------------------------------------------------------
CREATE TABLE IF NOT EXISTS tags (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS dataset_tags (
    dataset_id      INTEGER NOT NULL REFERENCES datasets(id),
    tag_id          INTEGER NOT NULL REFERENCES tags(id),
    PRIMARY KEY (dataset_id, tag_id)
);

-----------------------------------------------------------
-- PROJECTS: which projects use which datasets.
-----------------------------------------------------------
CREATE TABLE IF NOT EXISTS projects (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL UNIQUE,        -- e.g. "Fall-Detector", "Pose-Detection"
    path            TEXT,                        -- cluster path
    description     TEXT
);

CREATE TABLE IF NOT EXISTS project_datasets (
    project_id      INTEGER NOT NULL REFERENCES projects(id),
    dataset_id      INTEGER NOT NULL REFERENCES datasets(id),
    role            TEXT,                        -- train | eval | test | reference
    PRIMARY KEY (project_id, dataset_id)
);

-----------------------------------------------------------
-- INDEXES
-----------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_datasets_modality ON datasets(modality);
CREATE INDEX IF NOT EXISTS idx_datasets_domain ON datasets(domain);
CREATE INDEX IF NOT EXISTS idx_storage_dataset ON storage_locations(dataset_id);
CREATE INDEX IF NOT EXISTS idx_annotations_dataset ON annotations(dataset_id);
CREATE INDEX IF NOT EXISTS idx_lineage_parent ON lineage(parent_id);
CREATE INDEX IF NOT EXISTS idx_lineage_child ON lineage(child_id);
