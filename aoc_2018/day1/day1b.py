#!/usr/bin/env python

with open('day1a.txt') as f:
    # read data in and convert to integers
    l_freq = map( int, f.read().rstrip().split('\n') )


d_freq_seen = {}

# starting frequency
f = 0
d_freq_seen[f] = True
f_duplicate = None

while True:
    for adjust in l_freq:
        f += adjust
        if f in d_freq_seen:
            f_duplicate = f
            break
        else:
            d_freq_seen[f] = True

    # didn't find a duplicate frequency, so run through loop again
    if f_duplicate:
        break

print(f_duplicate)
