#!/bin/bash

BASE_URL="localhost:9200"
URL="${BASE_URL}/test/hellowworld/1"
HEADER='Content-Type: application/json'
curl -X POST -H $HEADER \
$URL \
-d '{"message": "hello world!"}'

