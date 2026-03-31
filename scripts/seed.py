"""Seed the catalog with all known datasets. Auto-generated from catalog.db."""

from data_catalog.db import init_db


def seed():
    conn = init_db()
    cur = conn.cursor()

    def ds(name):
        return cur.execute("SELECT id FROM datasets WHERE name=?", (name,)).fetchone()[0]

    def tag(name):
        return cur.execute("SELECT id FROM tags WHERE name=?", (name,)).fetchone()[0]

    def proj(name):
        return cur.execute("SELECT id FROM projects WHERE name=?", (name,)).fetchone()[0]

    # ── Datasets (36) ─────────────────────────────────
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('robinovich', '300 real-world fall videos with temporal fall annotations. Variable resolutions (320x240 to 1920x1080), variable FPS (7.5-30).', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('le2i', '190 fall-detection videos from 6 indoor scenes (coffee rooms, homes, lecture room, office). 320x240 AVI, 25 fps. 4 of 6 scenes have per-frame bounding-box annotations.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('fall-signal', 'Accelerometer + geophone sensor data from instrumented helmets. 3 sessions: 1 controlled trial + 2 basketball games. 1kHz sample rate CSV files with manual fall annotations in Excel.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('histotripsy-ct', 'CT DICOM scans from 2 histotripsy patients, 3 timepoints each (pre, 1d post, 4-6d post). 1,990 DICOM slices total. 512x512 pixel arrays with contrast enhancement.', 'image', 'histotripsy', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('histotripsy-us', 'Ultrasound videos from 2 histotripsy patients. Patient 1: 356MB mkv (250K frames, 60fps, ~70min). Patient 2: 956MB mp4 (171K frames, 60fps, ~48min).', 'video', 'histotripsy', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('har-up', 'UP-Fall Detection (HAR-UP) dataset. 1,111 recordings of 17 subjects performing 11 activities (5 fall types + 6 ADL). 3 trials per activity, 2 camera angles. Original format: PNG image sequences in ZIP archives.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ku-leuven-rdr', 'Ku Leuven RDR multi-camera fall detection dataset. ~270 AVI files, 12+ falls recorded from 5 camera angles each.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ur-fall-detection', 'UR Fall Detection Data Set. 40 ADL + 60 fall MP4 sequences. Dual-camera (cam0, cam1). 30 fall events from 2 angles.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('multiple-cameras-fall', 'Multiple Cameras Fall Data Set. 3.5GB dataset/ folder + metadata CSV + technical report PDF.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('sisfall', 'SisFall dataset. Accelerometer + gyroscope fall/ADL data. ZIP archive + CSV metadata.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('friendship-room', 'Avigilon security camera recordings from friendship/fall study sessions. 27 MP4 files organized by date (Feb-Mar 2026). Includes fall video analysis questionnaire + FVAQ spreadsheet.', 'video', 'friendship-study', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('friendship-faro', 'FARO 3D room scans of the friendship study environment. 8 scan positions, FLS scan files + FPC point clouds. 2.6GB main ZIP archive + uncompressed project files.', 'point-cloud', 'friendship-study', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('robinovich-pose-yolo11', 'YOLO11-Large pose estimation keypoints for all 300 Robinovich videos. 17 COCO keypoints per frame per person. 300 per-video JSONs + 300 annotated skeleton overlay videos.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('robinovich-pose-annotated', 'Robinovich fall videos with YOLO11-Large skeleton overlays. 300 MP4s with 17-keypoint COCO pose drawn on each frame.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('sisfall-videos', 'SisFall demo videos from YouTube. 19 ADL activity videos + 15 fall type videos. One video per activity/fall type showing the recording setup.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('sisfall-pose-yolo11', 'YOLO11-Large pose estimation keypoints for all 34 SisFall demo videos. 17 COCO keypoints per frame per person. 34 per-video JSONs + 34 annotated skeleton overlay videos.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('sisfall-pose-annotated', 'SisFall demo videos with YOLO11-Large skeleton overlays. 34 MP4s with 17-keypoint COCO pose drawn on each frame.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ur-fall-adl-depth', 'UR Fall Detection ADL sequences, depth/IR view only. 40 videos at 320x240, 30fps. Left half of original side-by-side videos.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ur-fall-adl-rgb', 'UR Fall Detection ADL sequences, RGB view only. 40 videos at 320x240, 30fps. Right half of original side-by-side videos.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ur-fall-falls-depth', 'UR Fall Detection fall sequences, depth/IR view only. 60 videos (30 falls x 2 cameras) at 320x240, 30fps.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ur-fall-falls-rgb', 'UR Fall Detection fall sequences, RGB view only. 60 videos (30 falls x 2 cameras) at 320x240, 30fps.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ur-fall-rgb-pose-yolo11', 'YOLO11-Large pose estimation keypoints for all 100 UR Fall RGB videos (40 ADL + 60 fall sequences). 17 COCO keypoints per frame per person.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ur-fall-rgb-pose-annotated', 'UR Fall RGB videos with YOLO11-Large skeleton overlays. 100 MP4s (40 ADL + 60 falls) at 320x240.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('multicam-fall-pose-yolo11', 'YOLO11-Large pose estimation keypoints for all 192 Multiple Cameras Fall videos (24 scenes x 8 cameras). 17 COCO keypoints per frame per person.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('multicam-fall-pose-annotated', 'Multiple Cameras Fall videos with YOLO11-Large skeleton overlays. 192 MP4s (24 scenes x 8 cameras).', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('le2i-pose-yolo11', 'YOLO11-Large pose estimation for 173 Le2i fall detection videos. 17 COCO keypoints per frame with impact frame annotations. Includes per-video JSONs, annotated videos, contact sheets, kinematics, and predictions.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('le2i-pose-annotated', 'Le2i fall detection videos with YOLO11-Large skeleton overlays. 173 MP4s with impact frame highlighting.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('set-elderly', 'SetElderly image object detection dataset. 413 PNG images (640x480) of elderly individuals with YOLO-format bounding box labels. 272 images contain person detections (class 1), 141 are negative samples (empty labels). Single class: elderly person.', 'image', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('har-up-videos', 'UP-Fall Detection (HAR-UP) dataset stitched to MP4 video. 1,111 videos at ~15fps. 510 fall videos (Activity1-5) + 601 ADL videos (Activity6-11). 17 subjects x 11 activities x 3 trials x 2 cameras. H.264 encoded.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('har-up-falls', 'HAR-UP fall videos only. 510 MP4s at ~15fps. Activity1: falling forward (hands), Activity2: falling forward (knees), Activity3: falling backwards, Activity4: falling sideward, Activity5: falling sitting in empty chair. 17 subjects x 5 fall types x 3 trials x 2 cameras.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('har-up-adl', 'HAR-UP ADL videos only. 601 MP4s at ~15fps. Activity6: walking, Activity7: standing, Activity8: sitting, Activity9: picking up object, Activity10: jumping, Activity11: laying. 17 subjects x 6 ADL types x 3 trials x 2 cameras.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('har-up-falls-pose-yolo11', 'YOLO11-Large pose estimation for 509 HAR-UP fall videos. 17 COCO keypoints per frame per person. 5 fall types across 17 subjects.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('har-up-falls-pose-annotated', 'HAR-UP fall videos with YOLO11-Large skeleton overlays. 509 MP4s with 17-keypoint COCO pose drawn on each frame.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ku-leuven-pose-yolo11', 'YOLO11-Large pose estimation for all 270 Ku Leuven RDR fall videos. 17 COCO keypoints per frame per person. 55 falls x 5 cameras.', 'signal', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('ku-leuven-pose-annotated', 'Ku Leuven RDR fall videos with YOLO11-Large skeleton overlays. 270 MP4s with 17-keypoint COCO pose drawn on each frame.', 'video', 'fall-detection', None, None))
    cur.execute("""INSERT OR IGNORE INTO datasets (name, description, modality, domain, source_url, license) VALUES (?, ?, ?, ?, ?, ?)""",
        ('le2i-benchmark-5model', 'Full 5-model pose estimation benchmark on all 190 Le2i videos (2025-12-23). Models: YOLO11-Large, YOLO11-XLarge, RTMPose-Balanced, RTMPose-Performance, MediaPipe-Heavy. Contains consolidated keypoints (992MB JSON), benchmark summary CSV, model comparison, and annotated videos per model.', 'signal', 'fall-detection', None, None))

    # ── Dataset Stats (36) ─────────────────────────────
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('robinovich'), 300, 1181116006, 'mp4', 'mixed', None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('le2i'), 190, 18253611008, 'avi', '320x240', 25.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('fall-signal'), 22, 12025908428, 'csv', None, 1000.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('histotripsy-ct'), 1990, 1610612736, 'dcm', '512x512', None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('histotripsy-us'), 2, 1395864371, 'mkv/mp4', None, 60.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('har-up'), 1111, 295708498329, 'zip', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ku-leuven-rdr'), 270, 4563402752, 'avi', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-detection'), 100, 118111600, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('multiple-cameras-fall'), 192, 3790308638, 'avi', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('sisfall'), 5, 225485783, 'zip', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('friendship-room'), 27, 6764573491, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('friendship-faro'), 105, 4080218931, 'fls/fpc', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('robinovich-pose-yolo11'), 300, 4402341478, 'json', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('robinovich-pose-annotated'), 300, 3221225472, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('sisfall-videos'), 34, 27262976, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('sisfall-pose-yolo11'), 34, 359661568, 'json', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('sisfall-pose-annotated'), 34, 571473920, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-adl-depth'), 40, 16777216, 'mp4', '320x240', 30.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-adl-rgb'), 40, 5242880, 'mp4', '320x240', 30.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-falls-depth'), 60, 212860928, 'mp4', '320x240', 30.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-falls-rgb'), 60, 204472320, 'mp4', '320x240', 30.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-rgb-pose-yolo11'), 100, 462422016, 'json', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-rgb-pose-annotated'), 100, 859832320, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('multicam-fall-pose-yolo11'), 192, 783286272, 'json', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('multicam-fall-pose-annotated'), 192, 7623566950, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('le2i-pose-yolo11'), 173, 3328599654, 'json', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('le2i-pose-annotated'), 173, 324009984, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('set-elderly'), 413, 186646528, 'png', '640x480', None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('har-up-videos'), 1111, 1395864371, 'mp4', None, 15.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('har-up-falls'), 510, 644245094, 'mp4', None, 15.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('har-up-adl'), 601, 751619276, 'mp4', None, 15.0, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('har-up-falls-pose-yolo11'), 509, 1932735283, 'json', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('har-up-falls-pose-annotated'), 509, 1288490188, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ku-leuven-pose-yolo11'), 270, 3650722201, 'json', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('ku-leuven-pose-annotated'), 270, 9878424780, 'mp4', None, None, None))
    cur.execute("""INSERT OR REPLACE INTO dataset_stats (dataset_id, num_samples, total_size_bytes, format, resolution, fps, duration_sec) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (ds('le2i-benchmark-5model'), 190, 4617089843, 'json', None, None, None))

    # ── Storage Locations (46) ──────────────────────────
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('robinovich'), 'cluster', '/projects/helmetlab1/Fall-Detector/robinovich', 1, 1181116006, '300 mp4 files, flat directory'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('le2i'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/le2i', 1, 18253611008, 'Ground truth. 6 scene subdirs + impact tracking xlsx + falldataset-imvia.zip.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('le2i'), 'cluster', '/projects/helmetlab1/Fall-Detector/le2i', 0, 98566144, 'Smaller copy (94MB), 190 mp4 files — possibly re-encoded subset'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('fall-signal'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/fall-signal', 1, 12025908428, 'Ground truth. 3 session subdirs + Excel annotations.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('fall-signal'), 'cluster', '/projects/helmetlab1/Fall-Signal/data', 0, 12025908428, 'Original location in Fall-Signal project.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('histotripsy-ct'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/histotripsy', 1, 1610612736, 'Ground truth. ZIP archives + extracted DICOM cache for 2 patients x 3 timepoints.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('histotripsy-ct'), 'cluster', '/projects/helmetlab1/Histotripsy/data', 0, 3435973836, 'Original location in Histotripsy project (includes US videos too).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('histotripsy-us'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/histotripsy', 1, 1395864371, 'Ground truth. 2 US videos alongside CT data.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('histotripsy-us'), 'cluster', '/projects/helmetlab1/Histotripsy/data', 0, 1395864371, 'Original location in Histotripsy project.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('le2i'), 'sharepoint', 'https://virginiatech.sharepoint.com/sites/VirginiaTechHelmetLab-OlderAdultTBI > Data/Publically Avalible Fall Sets/Downloaded Data/Optimised spatio-temporal descriptors', 0, 26843545600, 'SharePoint copy of Le2i/IMVIA dataset. Same scenes as le2i_original.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('har-up'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/har-up/archives', 1, 295708498329, 'Ground truth. ZIP files per Subject-Activity-Trial-Camera.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('har-up'), 'sharepoint', 'https://virginiatech.sharepoint.com/sites/VirginiaTechHelmetLab-OlderAdultTBI > Data/Publically Avalible Fall Sets/Downloaded Data/Not Using HAR-UP Fall Dataset', 0, 295708498329, 'SharePoint copy.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ku-leuven-rdr'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ku-leuven/videos', 1, 4563402752, 'Ground truth. FallX_CamY.avi naming.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ku-leuven-rdr'), 'sharepoint', 'https://virginiatech.sharepoint.com/sites/VirginiaTechHelmetLab-OlderAdultTBI > Data/Publically Avalible Fall Sets/Downloaded Data/Ku Leuven RDR', 0, 4563402752, 'SharePoint copy.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-detection'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ur-fall/original', 1, 118111600, 'Ground truth. ADL + fall sequences.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-detection'), 'sharepoint', 'https://virginiatech.sharepoint.com/sites/VirginiaTechHelmetLab-OlderAdultTBI > Data/Publically Avalible Fall Sets/Downloaded Data/UR Fall Detection Data Set', 0, 118111600, 'SharePoint copy.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('multiple-cameras-fall'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/multiple-cameras-fall/dataset', 1, 3790308638, 'Ground truth.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('sisfall'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/sisfall/signals', 1, 225485783, 'Ground truth. ZIP + CSV.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('friendship-room'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/friendship/room-videos', 1, 6764573491, 'Ground truth. Date-organized Avigilon exports.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('friendship-room'), 'sharepoint', 'https://virginiatech.sharepoint.com/sites/VirginiaTechHelmetLab-OlderAdultTBI > Data/Friendship In Room', 0, 6764573491, 'SharePoint original.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('friendship-faro'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/friendship/faro-scans', 1, 4080218931, 'Ground truth. FARO scans + point clouds.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('friendship-faro'), 'sharepoint', 'https://virginiatech.sharepoint.com/sites/VirginiaTechHelmetLab-OlderAdultTBI > Friendship Information/FARO', 0, 4080218931, 'SharePoint original.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('robinovich-pose-yolo11'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/robinovich/pose-yolo11', 1, 4402341478, 'Ground truth. keypoints/ (300 JSONs, 1.1GB) + annotated_videos/ (300 MP4s, 3.0GB)'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('robinovich-pose-annotated'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/robinovich/pose-yolo11/annotated_videos', 1, 3221225472, 'YOLO11-Large skeleton overlay videos.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('sisfall-videos'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/sisfall/videos', 1, 27262976, '34 MP4s downloaded from YouTube. 19 ADL (D01-D19) + 15 Falls (F01-F15).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('sisfall-pose-yolo11'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/sisfall/pose-yolo11', 1, 931135488, 'Ground truth. keypoints/ (34 JSONs) + annotated_videos/ (34 MP4s).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('sisfall-pose-annotated'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/sisfall/pose-yolo11/annotated_videos', 1, 571473920, 'YOLO11-Large skeleton overlay videos.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-adl-depth'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ur-fall/adl-depth', 1, 16777216, 'Split from original UR Fall side-by-side videos. H.264 encoded.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-adl-rgb'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ur-fall/adl-rgb', 1, 5242880, 'Split from original UR Fall side-by-side videos. H.264 encoded.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-falls-depth'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ur-fall/falls-depth', 1, 212860928, 'Split from original UR Fall side-by-side videos. H.264 encoded.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-falls-rgb'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ur-fall/falls-rgb', 1, 204472320, 'Split from original UR Fall side-by-side videos. H.264 encoded.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-rgb-pose-yolo11'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ur-fall/rgb-pose-yolo11', 1, 1322254336, 'Ground truth. keypoints/ (100 JSONs) + annotated_videos/ (100 MP4s).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ur-fall-rgb-pose-annotated'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ur-fall/rgb-pose-yolo11/annotated_videos', 1, 859832320, 'YOLO11-Large skeleton overlay videos.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('multicam-fall-pose-yolo11'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/multiple-cameras-fall/pose-yolo11', 1, 8375186227, 'Ground truth. keypoints/ (192 JSONs) + annotated_videos/ (192 MP4s).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('multicam-fall-pose-annotated'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/multiple-cameras-fall/pose-yolo11/annotated_videos', 1, 7623566950, 'YOLO11-Large skeleton overlay videos.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('le2i-pose-yolo11'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/le2i/pose-yolo11', 1, 3328599654, 'Ground truth. per_video/ (173 JSONs), annotated_videos/ (173 MP4s), contact_sheets/, kinematics/, diagnosis/, prediction/.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('le2i-pose-annotated'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/le2i/pose-yolo11/annotated_videos', 1, 324009984, 'YOLO11-Large skeleton overlay videos with impact frame highlights.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('set-elderly'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/set-elderly/SetElderly', 1, 186646528, '413 PNGs + 413 TXT labels. Extracted from setElderly.zip.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('har-up-videos'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/har-up/videos', 1, 1395864371, '1,111 MP4s stitched from PNG image sequences at 15fps. H.264, ~1MB each.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('har-up-falls'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/har-up/falls', 1, 644245094, 'Symlinks to videos/ for Activity1-5 (fall types).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('har-up-adl'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/har-up/adl', 1, 751619276, 'Symlinks to videos/ for Activity6-11 (ADL types).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('har-up-falls-pose-yolo11'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/har-up/falls-pose-yolo11', 1, 3221225472, 'Ground truth. keypoints/ (509 JSONs, 1.8GB) + annotated_videos/ (509 MP4s, 1.2GB).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('har-up-falls-pose-annotated'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/har-up/falls-pose-yolo11/annotated_videos', 1, 1288490188, 'YOLO11-Large skeleton overlay videos.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ku-leuven-pose-yolo11'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ku-leuven/pose-yolo11', 1, 13529146982, 'Ground truth. keypoints/ (270 JSONs, 3.4GB) + annotated_videos/ (270 MP4s, 9.2GB).'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('ku-leuven-pose-annotated'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/ku-leuven/pose-yolo11/annotated_videos', 1, 9878424780, 'YOLO11-Large skeleton overlay videos.'))
    cur.execute("""INSERT OR IGNORE INTO storage_locations (dataset_id, location_type, path, is_primary, size_bytes, notes) VALUES (?, ?, ?, ?, ?, ?)""",
        (ds('le2i-benchmark-5model'), 'cluster', '/projects/helmetlab1/Data-Catalog/data/le2i/benchmark-5model', 1, 4617089843, 'Consolidated keypoints JSON (992MB), benchmark summary, model comparison, annotated videos for 5 model variants.'))

    # ── Annotations (7) ────────────────────────────────
    cur.execute("""INSERT OR IGNORE INTO annotations (dataset_id, name, annotation_type, format, path, num_annotations, created_by, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (ds('robinovich'), 'temporal_falls', 'temporal', 'json', '/projects/helmetlab1/Data-Catalog/data/robinovich/annotations/robinovich_annotations.json', 474, None, '474 fall events across 300 videos. Start/end frame + time.'))
    cur.execute("""INSERT OR IGNORE INTO annotations (dataset_id, name, annotation_type, format, path, num_annotations, created_by, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (ds('le2i'), 'bbox_per_frame', 'bbox', 'txt', '/projects/helmetlab1/Data-Catalog/data/le2i', 131, None, 'Per-frame bounding boxes + fall start/end frame. Only 4 of 6 scenes annotated (Coffee_room_01/02, Home_01/02).'))
    cur.execute("""INSERT OR IGNORE INTO annotations (dataset_id, name, annotation_type, format, path, num_annotations, created_by, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (ds('le2i'), 'impact_frame_tracking', 'temporal', 'xlsx', '/projects/helmetlab1/Data-Catalog/data/le2i/V2 Le2i Impact Frame Tracking.xlsx', None, None, 'Impact frame tracking spreadsheet (V2)'))
    cur.execute("""INSERT OR IGNORE INTO annotations (dataset_id, name, annotation_type, format, path, num_annotations, created_by, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (ds('fall-signal'), 'game_fall_labels', 'temporal', 'xlsx', '/projects/helmetlab1/Data-Catalog/data/fall-signal', 11, None, 'Manual stopwatch-timed fall labels for basketball games. 2.21.26 has 11 labeled falls. Requires time-offset correction.'))
    cur.execute("""INSERT OR IGNORE INTO annotations (dataset_id, name, annotation_type, format, path, num_annotations, created_by, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (ds('sisfall-videos'), 'filename_labels', 'classification', 'filename', '/projects/helmetlab1/Data-Catalog/data/sisfall/videos', 34, 'SisFall authors', 'Labels encoded in filenames. Videos prefixed "Fall F" contain a fall event. Videos prefixed "ADL D" are activities of daily living (no fall). 15 fall videos (F01-F15), 19 ADL videos (D01-D19).'))
    cur.execute("""INSERT OR IGNORE INTO annotations (dataset_id, name, annotation_type, format, path, num_annotations, created_by, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (ds('set-elderly'), 'yolo_bbox_labels', 'bbox', 'txt', '/projects/helmetlab1/Data-Catalog/data/set-elderly/SetElderly', 272, 'SetElderly authors', 'YOLO format: "class x_center y_center width height" per line. Single class (1 = elderly person). 272 positive images with bboxes, 141 negative (empty txt). One txt per png, matched by filename.'))
    cur.execute("""INSERT OR IGNORE INTO annotations (dataset_id, name, annotation_type, format, path, num_annotations, created_by, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (ds('har-up-videos'), 'activity_labels', 'classification', 'filename', '/projects/helmetlab1/Data-Catalog/data/har-up/videos', 1111, 'UP-Fall Detection Dataset (Universidad Panamericana)', 'Labels encoded in filenames. Activity1-5 = FALL, Activity6-11 = ADL. Activity1: falling forward (hands), Activity2: falling forward (knees), Activity3: falling backwards, Activity4: falling sideward, Activity5: falling sitting in empty chair, Activity6: walking, Activity7: standing, Activity8: sitting, Activity9: picking up object, Activity10: jumping, Activity11: laying. 510 fall videos, 601 ADL videos. 17 subjects x 3 trials x 2 cameras.'))

    # ── Lineage (25) ─────────────────────────────────
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('robinovich'), ds('robinovich-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3, ~120 FPS). Processed all frames of all 300 videos. Includes skeleton overlay annotated videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('robinovich'), ds('robinovich-pose-annotated'), 'augmented_from', 'YOLO11-Large pose skeleton overlay rendered on each frame.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('sisfall'), ds('sisfall-videos'), 'reformatted_from', 'Demo videos downloaded from YouTube links in SisFall dataset via yt-dlp.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('sisfall-videos'), ds('sisfall-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3, ~128 FPS).'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('sisfall-videos'), ds('sisfall-pose-annotated'), 'augmented_from', 'YOLO11-Large pose skeleton overlay rendered on each frame.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-detection'), ds('ur-fall-adl-depth'), 'reformatted_from', 'Cropped left half (320x240) from 640x240 side-by-side video. Depth/IR grayscale view.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-detection'), ds('ur-fall-adl-rgb'), 'reformatted_from', 'Cropped right half (320x240) from 640x240 side-by-side video. RGB color view.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-detection'), ds('ur-fall-falls-depth'), 'reformatted_from', 'Cropped left half (320x240) from 640x240 side-by-side video. Depth/IR grayscale view.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-detection'), ds('ur-fall-falls-rgb'), 'reformatted_from', 'Cropped right half (320x240) from 640x240 side-by-side video. RGB color view.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-adl-rgb'), ds('ur-fall-rgb-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3). ADL RGB sequences.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-falls-rgb'), ds('ur-fall-rgb-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3). Fall RGB sequences.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-adl-rgb'), ds('ur-fall-rgb-pose-annotated'), 'augmented_from', 'YOLO11-Large skeleton overlay on ADL RGB videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ur-fall-falls-rgb'), ds('ur-fall-rgb-pose-annotated'), 'augmented_from', 'YOLO11-Large skeleton overlay on fall RGB videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('multiple-cameras-fall'), ds('multicam-fall-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3, ~123 FPS). 24 scenes x 8 cameras.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('multiple-cameras-fall'), ds('multicam-fall-pose-annotated'), 'augmented_from', 'YOLO11-Large skeleton overlay on all 192 videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('le2i'), ds('le2i-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3). Includes impact frame body part mapping from Le2i labels.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('le2i'), ds('le2i-pose-annotated'), 'augmented_from', 'YOLO11-Large skeleton overlay with impact frame highlighting.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('har-up'), ds('har-up-videos'), 'reformatted_from', 'PNG image sequences stitched to H.264 MP4 at 15fps via ffmpeg. 276GB -> 1.3GB.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('har-up-videos'), ds('har-up-falls'), 'subset_of', 'Activity1-5 only (5 fall types). 510 of 1111 videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('har-up-videos'), ds('har-up-adl'), 'subset_of', 'Activity6-11 only (6 ADL types). 601 of 1111 videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('har-up-falls'), ds('har-up-falls-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3, ~124 FPS).'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('har-up-falls'), ds('har-up-falls-pose-annotated'), 'augmented_from', 'YOLO11-Large skeleton overlay on fall videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ku-leuven-rdr'), ds('ku-leuven-pose-yolo11'), 'augmented_from', 'YOLO11-Large pose estimation (17 COCO keypoints, conf=0.3, ~123 FPS).'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('ku-leuven-rdr'), ds('ku-leuven-pose-annotated'), 'augmented_from', 'YOLO11-Large skeleton overlay on all 270 videos.'))
    cur.execute("""INSERT OR IGNORE INTO lineage (parent_id, child_id, relationship, transform) VALUES (?, ?, ?, ?)""",
        (ds('le2i'), ds('le2i-benchmark-5model'), 'augmented_from', '5-model pose estimation benchmark (YOLO11-L, YOLO11-XL, RTMPose-Bal, RTMPose-Perf, MediaPipe-Heavy). All 190 Le2i videos processed with each model.'))

    # ── Tags (25) ────────────────────────────────────
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('fall-detection',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('indoor',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('real-world',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('multi-scene',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('temporal-annotations',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('signal',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('accelerometer',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('geophone',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('basketball',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('helmet',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('medical-imaging',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('ct',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('dicom',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('ultrasound',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('histotripsy',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('longitudinal',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('public-dataset',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('multi-camera',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('friendship-study',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('3d-scan',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('point-cloud',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('avigilon',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('pose-estimation',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('keypoints',))
    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", ('yolo11',))

    # ── Dataset Tags (135) ─────────────────────────────
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich'), tag('real-world')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich'), tag('temporal-annotations')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i'), tag('real-world')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i'), tag('multi-scene')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('fall-signal'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('fall-signal'), tag('real-world')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('fall-signal'), tag('signal')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('fall-signal'), tag('accelerometer')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('fall-signal'), tag('geophone')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('fall-signal'), tag('basketball')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('fall-signal'), tag('helmet')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-ct'), tag('medical-imaging')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-ct'), tag('ct')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-ct'), tag('dicom')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-ct'), tag('histotripsy')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-ct'), tag('longitudinal')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-us'), tag('medical-imaging')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-us'), tag('ultrasound')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-us'), tag('histotripsy')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('histotripsy-us'), tag('longitudinal')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-rdr'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-rdr'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-rdr'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-rdr'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-detection'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-detection'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-detection'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-detection'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multiple-cameras-fall'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multiple-cameras-fall'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multiple-cameras-fall'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall'), tag('signal')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-room'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-room'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-room'), tag('real-world')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-room'), tag('friendship-study')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-room'), tag('avigilon')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-faro'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-faro'), tag('friendship-study')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-faro'), tag('3d-scan')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('friendship-faro'), tag('point-cloud')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich-pose-yolo11'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich-pose-yolo11'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich-pose-yolo11'), tag('keypoints')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich-pose-yolo11'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich-pose-annotated'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich-pose-annotated'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('robinovich-pose-annotated'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-videos'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-videos'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-videos'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-yolo11'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-yolo11'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-yolo11'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-yolo11'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-annotated'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-annotated'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-annotated'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('sisfall-pose-annotated'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-adl-depth'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-adl-depth'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-adl-depth'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-adl-rgb'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-adl-rgb'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-adl-rgb'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-falls-depth'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-falls-depth'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-falls-depth'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-falls-rgb'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-falls-rgb'), tag('indoor')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-falls-rgb'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-yolo11'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-yolo11'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-yolo11'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-yolo11'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-annotated'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-annotated'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-annotated'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ur-fall-rgb-pose-annotated'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-yolo11'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-yolo11'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-yolo11'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-yolo11'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-yolo11'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-annotated'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-annotated'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-annotated'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-annotated'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('multicam-fall-pose-annotated'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-pose-yolo11'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-pose-yolo11'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-pose-yolo11'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-pose-annotated'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-pose-annotated'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-pose-annotated'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('set-elderly'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('set-elderly'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-videos'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-videos'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-videos'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-adl'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-adl'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-adl'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-yolo11'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-yolo11'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-yolo11'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-yolo11'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-annotated'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-annotated'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-annotated'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('har-up-falls-pose-annotated'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-yolo11'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-yolo11'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-yolo11'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-yolo11'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-yolo11'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-annotated'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-annotated'), tag('public-dataset')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-annotated'), tag('multi-camera')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-annotated'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('ku-leuven-pose-annotated'), tag('yolo11')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-benchmark-5model'), tag('fall-detection')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-benchmark-5model'), tag('pose-estimation')))
    cur.execute("INSERT OR IGNORE INTO dataset_tags (dataset_id, tag_id) VALUES (?, ?)", (ds('le2i-benchmark-5model'), tag('yolo11')))

    # ── Projects (7) ────────────────────────────────
    cur.execute("""INSERT OR IGNORE INTO projects (name, path, description) VALUES (?, ?, ?)""",
        ('Label-Software', '/projects/helmetlab1/Label-Software', 'Video annotation tool integrated with the Data Catalog'))
    cur.execute("""INSERT OR IGNORE INTO projects (name, path, description) VALUES (?, ?, ?)""",
        ('Pose-Detection', '/projects/helmetlab1/Pose-Detection', 'Pose estimation library (YOLO11, RTMPose, MediaPipe, DETRPose, ViTPose++)'))
    cur.execute("""INSERT OR IGNORE INTO projects (name, path, description) VALUES (?, ?, ?)""",
        ('Fall-Detector', '/projects/helmetlab1/Fall-Detector', '3D-CNN-ViT frame-level fall detection model'))
    cur.execute("""INSERT OR IGNORE INTO projects (name, path, description) VALUES (?, ?, ?)""",
        ('Fall-Signal', '/projects/helmetlab1/Fall-Signal', 'Unsupervised fall detection from accelerometer + geophone signals'))
    cur.execute("""INSERT OR IGNORE INTO projects (name, path, description) VALUES (?, ?, ?)""",
        ('Histotripsy', '/projects/helmetlab1/Histotripsy', 'CT + ultrasound feature analysis for treatment monitoring'))
    cur.execute("""INSERT OR IGNORE INTO projects (name, path, description) VALUES (?, ?, ?)""",
        ('Impact-Locations', '/projects/helmetlab1/Impact-Locations', 'Impact body part prediction from pose keypoint trajectories'))
    cur.execute("""INSERT OR IGNORE INTO projects (name, path, description) VALUES (?, ?, ?)""",
        ('Friendship-Study', None, 'Older adult friendship/fall study'))

    # ── Project Datasets (16) ──────────────────────────
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('robinovich-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('sisfall-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('ur-fall-rgb-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('multicam-fall-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('le2i-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('har-up-falls-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('ku-leuven-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Pose-Detection'), ds('le2i-benchmark-5model'), 'eval'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Fall-Detector'), ds('robinovich'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Fall-Detector'), ds('le2i'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Fall-Signal'), ds('fall-signal'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Histotripsy'), ds('histotripsy-ct'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Histotripsy'), ds('histotripsy-us'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Impact-Locations'), ds('le2i-pose-yolo11'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Friendship-Study'), ds('friendship-room'), 'train'))
    cur.execute("INSERT OR IGNORE INTO project_datasets (project_id, dataset_id, role) VALUES (?, ?, ?)", (proj('Friendship-Study'), ds('friendship-faro'), 'reference'))

    conn.commit()
    conn.close()
    print("Seeded catalog with 36 datasets, 46 locations, 7 annotations, 25 lineage, 25 tags, 7 projects.")


if __name__ == "__main__":
    seed()
