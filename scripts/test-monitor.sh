#!/bin/bash

test_look_path=$1

if [ -z "$test_look_path" ]; then
  test_look_path='src'
fi

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
  "$test_look_path"
