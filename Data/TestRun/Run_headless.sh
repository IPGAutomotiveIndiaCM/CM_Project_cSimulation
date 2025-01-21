#!/bin/bash

# Loop through files in the directory
for file in /home/dockeration/Startupfiles/Startup_Example_*; do
  # Check if the file exists to prevent errors in case no files match the pattern
  echo TEST RUN;
  if [[ -f "$file" ]]; then 
    # Run your command for each matching file
    echo inside if loop
    //home/dockeration/src/CarMaker.linux64 "$file" -v -screen -dstore
  fi
done
