#!/bin/bash

DURATION=7
DB_FILE=positions_`date +"%Y-%m-%d"`.db


rm -f $DB_FILE
./db_all.py $DB_FILE $DURATION 2>&1
