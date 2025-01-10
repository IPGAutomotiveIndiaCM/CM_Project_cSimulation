#!/bin/bash

# Check if any files match the pattern before entering the loop
shopt -s nullglob  # Enable nullglob to prevent glob pattern from being expanded if no files match

# Loop through files starting with 'Startup_' in the specified directory
for file in /var/lib/jenkins/workspace/cSimulation/Startupfiles/Startup_*; do
  if [[ -f "$file" ]]; then  # Check if it's a regular file
    echo "Processing file: $file"  # Optional: Print the file being processed
    /var/lib/jenkins/workspace/cSimulation/src/CarMaker.linux64 "$file" -v -screen -dstore
  fi
done

shopt -u nullglob  # Disable nullglob after the loop
