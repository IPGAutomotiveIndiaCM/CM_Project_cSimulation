#!/bin/bash
for file in /home/cloudSimulation/CSimulation/Startupfiles/*
do
  /home/cloudSimulation/CSimulation/src/CarMaker.linux64 "$file" -v -screen -dstore
done

