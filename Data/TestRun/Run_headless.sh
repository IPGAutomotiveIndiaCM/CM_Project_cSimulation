#!/bin/bash
for file in /home/dhrithi/dk1/startupfile/Startup_*; do
  if [[ -f "$file" ]]; then  # Check if it's a regular file
    /home/dhrithi/dk1/src/CarMaker.linux64 "$file" -v -screen -dstore
  fi
done
