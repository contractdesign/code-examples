#!/usr/bin/env python3

#import sys.intern

with open('enable1.txt') as f:
    words = f.read().splitlines()


def funnel( w, l_prev, l_solutions=[] ):
    for i in range(len(w)):
        s = w[0:i] + w[i+1:]
        
        if s in words:
            # s is a valid word, so continue recursion
            temp = l_prev[:]
            temp.append(s)
            funnel(s, temp)
        else:
            # not an invalid word, so terminate
            if l_prev:
                l_solutions.append(l_prev)
    return l_solutions

def _funnel(w):
    return funnel( w, [w] )

def test():
    for w in ['gnash', 'princesses', 'turntables']:
        print(w, max_funnel(w))

def max_funnel(w):
    s = _funnel(w)
    return map(lambda x: len(x), s)
#    return map(len, _funnel(w))

#print(max_funnel('princesses'))

#test()

print(max_funnel('turntables'))
#print(_funnel('turntables'))

#for s in _funnel('turntables'):
#    print(s)


