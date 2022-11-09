#!/bin/bash
source ~/venv/main/bin/activate

echo "Starting watchmedo"
watchmedo shell-command \
  --patterns "*.py" \
  --command src/main.py \
  src
