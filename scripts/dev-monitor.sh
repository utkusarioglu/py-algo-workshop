#!/bin/bash
source ~/venv/main/bin/activate

echo "Starting watchmedo for \`src/main.py\`…"
watchmedo shell-command \
  --patterns "*.py" \
  --recursive \
  --command src/main.py \
  src
