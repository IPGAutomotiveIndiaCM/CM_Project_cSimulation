#!/bin/bash
#cd /var/lib/jenkins/workspace/EXECUTABLE\ BUILD/CM_Project/
for file in /var/lib/jenkins/workspace/EXECUTABLE\ BUILD/CM_Project/Startupfiles/*
do
  /var/lib/jenkins/workspace/EXECUTABLE\ BUILD/CM_Project/src/CarMaker.linux64 "$file" -v -screen -dstore
done

