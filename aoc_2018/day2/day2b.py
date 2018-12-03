#!/usr/bin/env python

with open('day2a.txt') as f:
    data = f.read().rstrip().split('\n')

def count_diff( a, b ):
    '''
    return the number of character differences between strings a and b
    '''
    num_diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            num_diff += 1

    return num_diff


n = len(data)

# compare the words pairwise
for i in range(n):
    for j in range(i+1, n):
        a = data[i]
        b = data[j]
        d = count_diff(a,b)

        if d==1:
            # print result if the strings differ by 1 character
            print(a, b)

            l_common = []
            for i in range(len(a)):
                if a[i]==b[i]:
                    l_common.append(a[i])
            print(''.join(l_common))
            

    
