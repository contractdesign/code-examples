#!/usr/bin/env python

with open('day1a.txt') as f:
    # read data in and convert to integers
    data = map( int, f.read().rstrip().split('\n') )

# the resultant frequency is the sum of the frequencies
print(sum(data))

