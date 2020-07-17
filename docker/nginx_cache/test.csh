#!/bin/bash


CACHE=172.28.1.2

for((i=0; i<=100; i++));
do
http http://${CACHE}/index.html Connection:close
sleep 5
done

#http http://${CACHE}/pic1.jpg Connection:close
#sleep 100

#http http://${CACHE}/pic2.jpg Connection:close
#sleep 100

#http http://${CACHE}/pic3.jpg Connection:close
#sleep 100
