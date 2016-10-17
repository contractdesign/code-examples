#!/usr/bin/env python2.7

# csv_change_stations.py
#
# sample the API every 't_sample' seconds and print whenever a train enters or exits a station to STDOUT
#
# the output is recorded in a 'sqlite3' database with the following table structure:
# (time), (status), LineCode, TrainId, DirectionNum, SecondsAtLocation, StationCode, DestinationStationCode, CarCount, ServiceType
#

import httplib, urllib, base64
import json
import time
import os

import sqlite3
import sys

import datetime



def getData():
    '''get the JSON file containing train positions'''
    headers = {
        # TODO: remove API key 
    }

    params = urllib.urlencode({})

    try:
        conn = httplib.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/TrainPositions/TrainPositions?contentType={contentType}&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return data


def main( filename, t_sample ):

    # dictionary to record the current location of the train to see if it changed
    d_tid2cid = {}


    #
    # create a database with two tables: positions and trains
    #
    conn = sqlite3.connect( filename )
    c = conn.cursor()
    
    c.execute( '''CREATE TABLE positions
                 ( seconds INTEGER, trainid INTEGER, directionnum INTEGER, destinationstationcode INTEGER, circuitid INTEGER, secondsatlocation INTEGER )''')
  
    c.execute( '''CREATE TABLE trains
                  ( seconds INTEGER, trainid INTEGER, servicetype TEXT, linecode TEXT, carcount INTEGER)''' )


    while True:
        try:
            # http://stackoverflow.com/questions/15971308/get-seconds-since-midnight-in-python
            # compute midnight
            now = datetime.datetime.now()
            midnight = now.replace( hour=0, minute=0, second=0, microsecond=0 )

            t_sec = (now - midnight).seconds

            # get the most recent position data for the trains
            for pos in json.loads( getData() )['TrainPositions']:
                if pos['TrainId'] not in d_tid2cid.keys() or \
                   pos['CircuitId'] != d_tid2cid[ pos['TrainId'] ]:

                    if pos['TrainId'] not in d_tid2cid.keys():
                        # if train has not already been seen insert an entry into the "trains" table
                        c.execute( "INSERT INTO trains VALUES (?,?,?,?,?)",
                                   ( t_sec,
                                     pos['TrainId'],
                                     pos['ServiceType'],
                                     pos['LineCode'],
                                     pos['CarCount'] ) )
                        conn.commit()

                    # record its current position
                    c.execute( "INSERT INTO positions VALUES (?,?,?,?,?,?)",
                               (t_sec,
                                pos['TrainId'],
                                pos['DirectionNum'],
                                pos['DestinationStationCode'],
                                pos['CircuitId'],
                                pos['SecondsAtLocation'] ) )
                    conn.commit()

                    d_tid2cid[ pos['TrainId'] ] = pos['CircuitId']

            # delay polling 't_sample' seconds.  the WMATA system appears to update about every 10 seconds.
            time.sleep(float(t_sample))

        except KeyboardInterrupt:
            conn.close()


if __name__=='__main__':
    os.environ['TZ'] = 'America/New_York'

    # TODO add arguments
    main( sys.argv[1], sys.argv[2] )
