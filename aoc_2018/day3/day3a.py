#!/usr/bin/env python

with open('day3a.txt') as f:
    data = f.read().rstrip().split('\n')

l_rect = []
for d in data:
    fields = d.split()
    (x,y) = fields[2].rstrip(':').split(',')
    (l,w) = fields[3].split('x')
    l_rect.append( (x, y, l, w) )


d_rect = {}
for r in l_rect:
    (x, y, l, w) = int(r[0]), int(r[1]), int(r[2]), int(r[3])
    for i in range(l):
        for j in range(w):
            if (x+i, y+j) in d_rect:
                d_rect[ (x+i, y+j) ] += 1
            else:
                d_rect[ (x+i, y+j) ] = 1

num = 0
for k in d_rect:
    if d_rect[k]>1:
        num += 1

print num

            
        
