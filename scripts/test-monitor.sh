#!/bin/bash

echo "Starting watchmedo…"
watchmedo shell-command \
  --patterns "*.py" \
  --recursive \
  --command "\
    python -m unittest \
      discover \
      -s tests \
      -p='*_unit_test.py' \
    " \
  .
  
