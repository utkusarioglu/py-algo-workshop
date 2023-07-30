#!/bin/bash

echo "Starting watchmedo for pytest…"
watchmedo shell-command \
  --patterns "*.py" \
  --recursive \
  --wait \
  --verbose \
  --command '
      if [ "${watch_event_type}" = "closed" ]; then
        pytest src/network_delay 
      fi
    '\
  src
