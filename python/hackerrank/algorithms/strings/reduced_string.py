#!/usr/bin/env python2.7

# https://www.hackerrank.com/challenges/reduced-string

import re

def reduce( s ):
    m = ''
    while True:
        m = re.sub( r'(.)\1{1}', r'', s )
        if m==s:
            break
        else:
            s = m
    if m=='':
        return 'Empty String'
    else:
        return m


for s in ['baab', 'aa']:
    print reduce( s )
        
