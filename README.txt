Urban Mission Planning Challenge - Solution
============================================

Pipeline:
  1. Load satellite imagery (1500x1500 RGB TIFF) and road masks
  2. Train U-Net (ResNet34 encoder) for road segmentation on 512x512 patches
  3. Sliding-window inference to produce full-resolution road probability maps
  4. Build cost map (cheap on-road, expensive off-road) from predicted mask
  5. Dijkstra shortest path from start to goal on cost map
  6. Generate submission JSON

Files:
  solution.ipynb   - Main notebook (Colab-ready, run all cells in order)
  requirements.txt - Python dependencies
  submission.json  - Generated output (when test start/goal coords are available)

Usage:
  1. Open solution.ipynb in Google Colab or Jupyter
  2. Ensure ump_data/ directory is accessible (upload or mount)
  3. Run all cells in order
  4. Training: ~5-8 min on Colab T4 GPU
  5. When test start/goal coordinates are released, run the submission cell

Scoring: 1000 - PathLength - 50 x Violations
  Violations cost 50x more than path length, so staying on-road is critical.

Coordinate convention:
  JSON / submission: [x, y] (column, row)
  NumPy arrays:      [y, x] (row, column)
  PIL pixel access:  (x, y) (column, row)
