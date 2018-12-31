#!/usr/bin/env python

with open('day2a.txt') as f:
    data = f.read().rstrip().split('\n')


def compute_repeats( s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    repeat_2 = False
    repeat_3 = False
    
    for k in d.keys():
        if d[k]==2:
            repeat_2 = repeat_2 or True
        if d[k]==3:
            repeat_3 = repeat_3 or True
    return (repeat_2, repeat_3)

num_2 = 0
num_3 = 0
for d in data:
    r = compute_repeats(d)

    print(r,d)
    if r[0]:
        num_2 += 1
    if r[1]:
        num_3 += 1

print( num_2*num_3 )
