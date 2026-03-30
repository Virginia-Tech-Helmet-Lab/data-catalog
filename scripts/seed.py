"""Seed the catalog with all known datasets."""

from src.data_catalog.db import init_db


def seed():
    conn = init_db()
    cur = conn.cursor()

    # ── Datasets ──────────────────────────────────────────────
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url)
           VALUES (?, ?, ?, ?, ?)""",
        (
            "robinovich",
            "300 real-world fall videos with temporal fall annotations. "
            "Variable resolutions (320x240 to 1920x1080), variable FPS (7.5-30).",
            "video",
            "fall-detection",
            None,
        ),
    )
    robinovich_id = cur.execute(
        "SELECT id FROM datasets WHERE name='robinovich'"
    ).fetchone()[0]

    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url)
           VALUES (?, ?, ?, ?, ?)""",
        (
            "le2i",
            "190 fall-detection videos from 6 indoor scenes (coffee rooms, homes, "
            "lecture room, office). 320x240 AVI, 25 fps. 4 of 6 scenes have "
            "per-frame bounding-box annotations.",
            "video",
            "fall-detection",
            None,
        ),
    )
    le2i_id = cur.execute(
        "SELECT id FROM datasets WHERE name='le2i'"
    ).fetchone()[0]

    # ── Dataset stats ─────────────────────────────────────────
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (robinovich_id, 300, int(1.1 * 1024**3), "mp4", "mixed", None, None),
    )
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (le2i_id, 190, int(17 * 1024**3), "avi", "320x240", 25.0, None),
    )

    # ── Storage locations ─────────────────────────────────────
    # Robinovich: 1 known location
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            robinovich_id,
            "cluster",
            "/projects/helmetlab1/Fall-Detector/robinovich",
            1,
            int(1.1 * 1024**3),
            "300 mp4 files, flat directory",
        ),
    )

    # Le2i: 2 known locations
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            le2i_id,
            "cluster",
            "/projects/helmetlab1/Pose-Detection/data/le2i_original",
            1,
            int(17 * 1024**3),
            "Full dataset: 6 scene subdirs, avi + txt annotations",
        ),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            le2i_id,
            "cluster",
            "/projects/helmetlab1/Fall-Detector/le2i",
            0,
            int(94 * 1024**2),
            "Smaller copy (94MB), 190 mp4 files — possibly re-encoded subset",
        ),
    )

    # ── Annotations ───────────────────────────────────────────
    cur.execute(
        """INSERT OR IGNORE INTO annotations
           (dataset_id, name, annotation_type, format, path, num_annotations, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            robinovich_id,
            "temporal_falls",
            "temporal",
            "json",
            "/projects/helmetlab1/Fall-Detector/data_stats/robinovich_annotations.json",
            474,
            "474 fall events across 300 videos. Start/end frame + time.",
        ),
    )
    cur.execute(
        """INSERT OR IGNORE INTO annotations
           (dataset_id, name, annotation_type, format, path, num_annotations, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            le2i_id,
            "bbox_per_frame",
            "bbox",
            "txt",
            "/projects/helmetlab1/Pose-Detection/data/le2i_original",
            131,
            "Per-frame bounding boxes + fall start/end frame. "
            "Only 4 of 6 scenes annotated (Coffee_room_01/02, Home_01/02).",
        ),
    )
    cur.execute(
        """INSERT OR IGNORE INTO annotations
           (dataset_id, name, annotation_type, format, path, num_annotations, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            le2i_id,
            "impact_frame_tracking",
            "temporal",
            "xlsx",
            "/projects/helmetlab1/Pose-Detection/data/V2 Le2i Impact Frame Tracking.xlsx",
            None,
            "Impact frame tracking spreadsheet (V2)",
        ),
    )

    # ── Projects ──────────────────────────────────────────────
    cur.execute(
        """INSERT OR IGNORE INTO projects (name, path, description)
           VALUES (?, ?, ?)""",
        (
            "Fall-Detector",
            "/projects/helmetlab1/Fall-Detector",
            "3D-CNN-ViT fall detection model (X3D + DeiT-Small)",
        ),
    )
    fall_detector_id = cur.execute(
        "SELECT id FROM projects WHERE name='Fall-Detector'"
    ).fetchone()[0]

    cur.execute(
        """INSERT OR IGNORE INTO projects (name, path, description)
           VALUES (?, ?, ?)""",
        (
            "Pose-Detection",
            "/projects/helmetlab1/Pose-Detection",
            "Pose estimation testing framework (YOLO11-Pose, RTMPose, etc.)",
        ),
    )
    pose_detection_id = cur.execute(
        "SELECT id FROM projects WHERE name='Pose-Detection'"
    ).fetchone()[0]

    # ── Project <-> Dataset links ─────────────────────────────
    for project_id, dataset_id, role in [
        (fall_detector_id, robinovich_id, "train"),
        (fall_detector_id, le2i_id, "train"),
        (pose_detection_id, le2i_id, "eval"),
    ]:
        cur.execute(
            """INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role)
               VALUES (?, ?, ?)""",
            (project_id, dataset_id, role),
        )

    # ── Tags ──────────────────────────────────────────────────
    tag_names = ["fall-detection", "indoor", "real-world", "multi-scene", "temporal-annotations"]
    for tag_name in tag_names:
        cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag_name,))

    def tag_dataset(dataset_id, tag_list):
        for t in tag_list:
            tag_id = cur.execute("SELECT id FROM tags WHERE name=?", (t,)).fetchone()[0]
            cur.execute(
                "INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)",
                (dataset_id, tag_id),
            )

    tag_dataset(robinovich_id, ["fall-detection", "indoor", "real-world", "temporal-annotations"])
    tag_dataset(le2i_id, ["fall-detection", "indoor", "real-world", "multi-scene"])

    # ══════════════════════════════════════════════════════════
    # FALL-SIGNAL
    # ══════════════════════════════════════════════════════════
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "fall-signal",
            "Accelerometer + geophone sensor data from instrumented helmets. "
            "3 sessions: 1 controlled trial + 2 basketball games. "
            "1kHz sample rate CSV files with manual fall annotations in Excel.",
            "signal",
            "fall-detection",
        ),
    )
    fall_signal_id = cur.execute(
        "SELECT id FROM datasets WHERE name='fall-signal'"
    ).fetchone()[0]

    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format, resolution, fps)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (fall_signal_id, 22, int(11.2 * 1024**3), "csv", None, 1000.0),
    )

    # Primary location: Data-Catalog
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            fall_signal_id,
            "cluster",
            "/projects/helmetlab1/Data-Catalog/data/fall-signal",
            1,
            int(11.2 * 1024**3),
            "Ground truth. 3 session subdirs + Excel annotations.",
        ),
    )
    # Copy location
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            fall_signal_id,
            "cluster",
            "/projects/helmetlab1/Fall-Signal/data",
            0,
            int(11.2 * 1024**3),
            "Original location in Fall-Signal project.",
        ),
    )

    # Annotations
    cur.execute(
        """INSERT OR IGNORE INTO annotations
           (dataset_id, name, annotation_type, format, path, num_annotations, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            fall_signal_id,
            "game_fall_labels",
            "temporal",
            "xlsx",
            "/projects/helmetlab1/Data-Catalog/data/fall-signal",
            11,
            "Manual stopwatch-timed fall labels for basketball games. "
            "2.21.26 has 11 labeled falls. Requires time-offset correction.",
        ),
    )

    # Project
    cur.execute(
        """INSERT OR IGNORE INTO projects (name, path, description)
           VALUES (?, ?, ?)""",
        (
            "Fall-Signal",
            "/projects/helmetlab1/Fall-Signal",
            "Unsupervised fall detection from accelerometer + geophone signals",
        ),
    )
    fall_signal_proj_id = cur.execute(
        "SELECT id FROM projects WHERE name='Fall-Signal'"
    ).fetchone()[0]
    cur.execute(
        "INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)",
        (fall_signal_proj_id, fall_signal_id, "train"),
    )

    # Tags
    for t in ["signal", "accelerometer", "geophone", "basketball", "helmet"]:
        cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (t,))
    tag_dataset(fall_signal_id, ["fall-detection", "real-world", "signal", "accelerometer", "geophone", "basketball", "helmet"])

    # ══════════════════════════════════════════════════════════
    # HISTOTRIPSY
    # ══════════════════════════════════════════════════════════

    # CT dataset
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "histotripsy-ct",
            "CT DICOM scans from 2 histotripsy patients, 3 timepoints each "
            "(pre, 1d post, 4-6d post). 1,990 DICOM slices total. "
            "512x512 pixel arrays with contrast enhancement.",
            "image",
            "histotripsy",
        ),
    )
    histo_ct_id = cur.execute(
        "SELECT id FROM datasets WHERE name='histotripsy-ct'"
    ).fetchone()[0]

    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format, resolution)
           VALUES (?, ?, ?, ?, ?)""",
        (histo_ct_id, 1990, int(1.5 * 1024**3), "dcm", "512x512"),
    )

    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            histo_ct_id,
            "cluster",
            "/projects/helmetlab1/Data-Catalog/data/histotripsy",
            1,
            int(1.5 * 1024**3),
            "Ground truth. ZIP archives + extracted DICOM cache for 2 patients x 3 timepoints.",
        ),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            histo_ct_id,
            "cluster",
            "/projects/helmetlab1/Histotripsy/data",
            0,
            int(3.2 * 1024**3),
            "Original location in Histotripsy project (includes US videos too).",
        ),
    )

    # US dataset
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "histotripsy-us",
            "Ultrasound videos from 2 histotripsy patients. "
            "Patient 1: 356MB mkv (250K frames, 60fps, ~70min). "
            "Patient 2: 956MB mp4 (171K frames, 60fps, ~48min).",
            "video",
            "histotripsy",
        ),
    )
    histo_us_id = cur.execute(
        "SELECT id FROM datasets WHERE name='histotripsy-us'"
    ).fetchone()[0]

    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format, resolution, fps)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (histo_us_id, 2, int(1.3 * 1024**3), "mkv/mp4", None, 60.0),
    )

    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            histo_us_id,
            "cluster",
            "/projects/helmetlab1/Data-Catalog/data/histotripsy",
            1,
            int(1.3 * 1024**3),
            "Ground truth. 2 US videos alongside CT data.",
        ),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            histo_us_id,
            "cluster",
            "/projects/helmetlab1/Histotripsy/data",
            0,
            int(1.3 * 1024**3),
            "Original location in Histotripsy project.",
        ),
    )

    # Histotripsy project
    cur.execute(
        """INSERT OR IGNORE INTO projects (name, path, description)
           VALUES (?, ?, ?)""",
        (
            "Histotripsy",
            "/projects/helmetlab1/Histotripsy",
            "CT + US feature analysis pipeline for histotripsy treatment monitoring",
        ),
    )
    histo_proj_id = cur.execute(
        "SELECT id FROM projects WHERE name='Histotripsy'"
    ).fetchone()[0]
    cur.execute(
        "INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)",
        (histo_proj_id, histo_ct_id, "train"),
    )
    cur.execute(
        "INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)",
        (histo_proj_id, histo_us_id, "train"),
    )

    # Tags
    for t in ["medical-imaging", "ct", "dicom", "ultrasound", "histotripsy", "longitudinal"]:
        cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (t,))
    tag_dataset(histo_ct_id, ["medical-imaging", "ct", "dicom", "histotripsy", "longitudinal"])
    tag_dataset(histo_us_id, ["medical-imaging", "ultrasound", "histotripsy", "longitudinal"])

    # ══════════════════════════════════════════════════════════
    # PUBLIC FALL SETS (from SharePoint)
    # ══════════════════════════════════════════════════════════

    SP_BASE = "https://virginiatech.sharepoint.com/sites/VirginiaTechHelmetLab-OlderAdultTBI"

    # -- Le2i: add SharePoint as additional storage location --
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            le2i_id,
            "sharepoint",
            f"{SP_BASE} > Data/Publically Avalible Fall Sets/Downloaded Data/Optimised spatio-temporal descriptors",
            0,
            int(25 * 1024**3),
            "SharePoint copy of Le2i/IMVIA dataset. Same scenes as le2i_original.",
        ),
    )

    # -- HAR-UP --
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "har-up",
            "HAR-UP Fall Dataset. 1,111 ZIP archives of video clips organized by "
            "Subject-Activity-Trial-Camera. Human activity recognition with falls.",
            "video",
            "fall-detection",
        ),
    )
    harup_id = cur.execute("SELECT id FROM datasets WHERE name='har-up'").fetchone()[0]
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format)
           VALUES (?, ?, ?, ?)""",
        (harup_id, 1111, int(275.4 * 1024**3), "zip"),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (harup_id, "cluster",
         "/projects/helmetlab1/Data-Catalog/data/public-fall-sets/har-up",
         1, int(275.4 * 1024**3), "Ground truth. ZIP files per Subject-Activity-Trial-Camera."),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (harup_id, "sharepoint",
         f"{SP_BASE} > Data/Publically Avalible Fall Sets/Downloaded Data/Not Using HAR-UP Fall Dataset",
         0, int(275.4 * 1024**3), "SharePoint copy."),
    )

    # -- Ku Leuven RDR --
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "ku-leuven-rdr",
            "Ku Leuven RDR multi-camera fall detection dataset. "
            "~270 AVI files, 12+ falls recorded from 5 camera angles each.",
            "video",
            "fall-detection",
        ),
    )
    kuleuven_id = cur.execute("SELECT id FROM datasets WHERE name='ku-leuven-rdr'").fetchone()[0]
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format)
           VALUES (?, ?, ?, ?)""",
        (kuleuven_id, 270, int(4.25 * 1024**3), "avi"),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (kuleuven_id, "cluster",
         "/projects/helmetlab1/Data-Catalog/data/public-fall-sets/ku-leuven-rdr",
         1, int(4.25 * 1024**3), "Ground truth. FallX_CamY.avi naming."),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (kuleuven_id, "sharepoint",
         f"{SP_BASE} > Data/Publically Avalible Fall Sets/Downloaded Data/Ku Leuven RDR",
         0, int(4.25 * 1024**3), "SharePoint copy."),
    )

    # -- UR Fall Detection --
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "ur-fall-detection",
            "UR Fall Detection Data Set. 40 ADL + 60 fall MP4 sequences. "
            "Dual-camera (cam0, cam1). 30 fall events from 2 angles.",
            "video",
            "fall-detection",
        ),
    )
    urfall_id = cur.execute("SELECT id FROM datasets WHERE name='ur-fall-detection'").fetchone()[0]
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format)
           VALUES (?, ?, ?, ?)""",
        (urfall_id, 100, int(0.11 * 1024**3), "mp4"),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (urfall_id, "cluster",
         "/projects/helmetlab1/Data-Catalog/data/public-fall-sets/ur-fall-detection",
         1, int(0.11 * 1024**3), "Ground truth. ADL + fall sequences."),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (urfall_id, "sharepoint",
         f"{SP_BASE} > Data/Publically Avalible Fall Sets/Downloaded Data/UR Fall Detection Data Set",
         0, int(0.11 * 1024**3), "SharePoint copy."),
    )

    # -- Multiple Cameras Fall --
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "multiple-cameras-fall",
            "Multiple Cameras Fall Data Set. 3.5GB dataset/ folder + metadata CSV + technical report PDF.",
            "video",
            "fall-detection",
        ),
    )
    multicam_id = cur.execute("SELECT id FROM datasets WHERE name='multiple-cameras-fall'").fetchone()[0]
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format)
           VALUES (?, ?, ?, ?)""",
        (multicam_id, 3, int(3.53 * 1024**3), "mixed"),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (multicam_id, "cluster",
         "/projects/helmetlab1/Data-Catalog/data/public-fall-sets/multiple-cameras-fall",
         1, int(3.53 * 1024**3), "Ground truth."),
    )

    # -- SisFall --
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "sisfall",
            "SisFall dataset. Accelerometer + gyroscope fall/ADL data. "
            "ZIP archive + CSV metadata.",
            "signal",
            "fall-detection",
        ),
    )
    sisfall_id = cur.execute("SELECT id FROM datasets WHERE name='sisfall'").fetchone()[0]
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format)
           VALUES (?, ?, ?, ?)""",
        (sisfall_id, 5, int(0.21 * 1024**3), "zip"),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (sisfall_id, "cluster",
         "/projects/helmetlab1/Data-Catalog/data/public-fall-sets/sisfall",
         1, int(0.21 * 1024**3), "Ground truth. ZIP + CSV."),
    )

    # Tags for public fall sets
    for t in ["public-dataset", "multi-camera"]:
        cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (t,))
    tag_dataset(harup_id, ["fall-detection", "public-dataset"])
    tag_dataset(kuleuven_id, ["fall-detection", "public-dataset", "multi-camera", "indoor"])
    tag_dataset(urfall_id, ["fall-detection", "public-dataset", "multi-camera", "indoor"])
    tag_dataset(multicam_id, ["fall-detection", "public-dataset", "multi-camera"])
    tag_dataset(sisfall_id, ["fall-detection", "public-dataset", "signal"])

    # ══════════════════════════════════════════════════════════
    # FRIENDSHIP DATASETS (from SharePoint)
    # ══════════════════════════════════════════════════════════

    # -- Friendship Room --
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "friendship-room",
            "Avigilon security camera recordings from friendship/fall study sessions. "
            "27 MP4 files organized by date (Feb-Mar 2026). "
            "Includes fall video analysis questionnaire + FVAQ spreadsheet.",
            "video",
            "friendship-study",
        ),
    )
    friend_room_id = cur.execute("SELECT id FROM datasets WHERE name='friendship-room'").fetchone()[0]
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format)
           VALUES (?, ?, ?, ?)""",
        (friend_room_id, 27, int(6.3 * 1024**3), "mp4"),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (friend_room_id, "cluster",
         "/projects/helmetlab1/Data-Catalog/data/friendship-room",
         1, int(6.3 * 1024**3), "Ground truth. Date-organized Avigilon exports."),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (friend_room_id, "sharepoint",
         f"{SP_BASE} > Data/Friendship In Room",
         0, int(6.3 * 1024**3), "SharePoint original."),
    )

    # -- Friendship FARO --
    cur.execute(
        """INSERT OR IGNORE INTO datasets (name, description, modality, domain)
           VALUES (?, ?, ?, ?)""",
        (
            "friendship-faro",
            "FARO 3D room scans of the friendship study environment. "
            "8 scan positions, FLS scan files + FPC point clouds. "
            "2.6GB main ZIP archive + uncompressed project files.",
            "point-cloud",
            "friendship-study",
        ),
    )
    friend_faro_id = cur.execute("SELECT id FROM datasets WHERE name='friendship-faro'").fetchone()[0]
    cur.execute(
        """INSERT OR REPLACE INTO dataset_stats
           (dataset_id, num_samples, total_size_bytes, format)
           VALUES (?, ?, ?, ?)""",
        (friend_faro_id, 105, int(3.8 * 1024**3), "fls/fpc"),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (friend_faro_id, "cluster",
         "/projects/helmetlab1/Data-Catalog/data/friendship-faro",
         1, int(3.8 * 1024**3), "Ground truth. FARO scans + point clouds."),
    )
    cur.execute(
        """INSERT OR IGNORE INTO storage_locations
           (dataset_id, location_type, path, is_primary, size_bytes, notes)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (friend_faro_id, "sharepoint",
         f"{SP_BASE} > Friendship Information/FARO",
         0, int(3.8 * 1024**3), "SharePoint original."),
    )

    # Friendship project + tags
    cur.execute(
        """INSERT OR IGNORE INTO projects (name, path, description)
           VALUES (?, ?, ?)""",
        ("Friendship-Study", None, "Older adult friendship/fall study with video + 3D room scans"),
    )
    friend_proj_id = cur.execute("SELECT id FROM projects WHERE name='Friendship-Study'").fetchone()[0]
    cur.execute(
        "INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)",
        (friend_proj_id, friend_room_id, "train"),
    )
    cur.execute(
        "INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)",
        (friend_proj_id, friend_faro_id, "reference"),
    )

    for t in ["friendship-study", "3d-scan", "point-cloud", "avigilon"]:
        cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (t,))
    tag_dataset(friend_room_id, ["fall-detection", "indoor", "real-world", "friendship-study", "avigilon"])
    tag_dataset(friend_faro_id, ["friendship-study", "3d-scan", "point-cloud", "indoor"])

    conn.commit()
    conn.close()
    print("Seeded catalog with all datasets.")


if __name__ == "__main__":
    seed()
