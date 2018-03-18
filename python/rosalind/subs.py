#!/usr/bin/env python2.7

# http://rosalind.info/problems/subs/
def find_subs( s, subs ):
    l_position = []
    len_subs = len(subs)
    for i in range(0, len(s) - len_subs):
        if s[i:i+len_subs]==subs:
            # note offset by 1
            l_position.append(i+1)

    return l_position



l_data = []
with open( 'rosalind_subs.txt' ) as f:
    l_data = map( lambda x: x.rstrip(), f.readlines() )

for i in find_subs( l_data[0], l_data[1] ):
    print i,
