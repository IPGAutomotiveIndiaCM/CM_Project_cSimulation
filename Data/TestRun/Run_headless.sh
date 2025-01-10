#!/bin/bash

# Loop through files in the directory
for file in /var/lib/jenkins/workspace/cSimulation/Startupfiles/Startup_Example_*; do
  # Check if the file exists to prevent errors in case no files match the pattern
  echo Hello World;
  if [[ -f "$file" ]]; then
    # Run your command for each matching file
    //var/lib/jenkins/workspace/cSimulation/src/CarMaker.linux64 "$file" -v -screen -dstore
  fi
done
