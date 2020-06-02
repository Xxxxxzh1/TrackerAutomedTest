#!/bin/bash

cd /home/zz/workspace/workspace/Tracker
repo sync
cd /home/zz/workspace/workspace/Tracker/build
make
echo "++++++++++++++++++ repo sync success! ++++++++++++++++++"