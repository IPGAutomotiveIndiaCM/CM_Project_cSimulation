#!/bin/bash
for file in /home/cSimulation/Startupfiles/*
do
  /home/cSimulation/src/CarMaker.linux64 "$file" -v -screen -dstore
done
chmod +x /home/export_movie.sh
/home/export_movie.sh


