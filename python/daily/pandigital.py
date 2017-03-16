#!/usr/bin/env python2.7

d_n = { 1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        5: 'V',
        4: 'IV',
        1: 'I' }
        
l_n = sorted(d_n.keys(), reverse=True)

def convert(i):
    '''convert a number n, 0 < n < 2000 to Roman numerals'''

    for n in l_n:
        if i >= n:
            return d_n[n] + convert(i - n)
    return ''


l_pandigital = sorted('IVXLCDM')
for i in range(1, 2000):
    roman = convert(i)
    if sorted(roman) == l_pandigital:
        print i, roman

    
    
