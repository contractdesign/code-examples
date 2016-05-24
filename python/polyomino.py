#!/usr/bin/env python2.7

import sys

#
# A polyomino is represented by a set of tuples representing integer
# coordinates.  For example, a line of two points
#    **
# is represented by
#    set([(0,0), (1,0)])
#
# 'set' is used to ensure that points are not repeated
#


def canonicalize( s_tuple ):
    '''return the polyominial in canonical form where it is shifted to
    the lower left'''

    min_x = min( [p[0] for p in s_tuple] )
    min_y = min( [p[1] for p in s_tuple] )

    return set([ (p[0] - min_x, p[1] - min_y) for p in s_tuple ])


def display( s_tuple ):
    '''print a polyomino to the screen'''
    temp = canonicalize(s_tuple)

    # find the extent, the lower left point is (0,0) b/c of
    # canonicalize
    max_x = max( [p[0] for p in temp] )
    max_y = max( [p[1] for p in temp] )

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x,y) in temp:
                sys.stdout.write( '*' )
            else:
                sys.stdout.write( ' ' )
        print ''
    
    

def addOne( s_tuple ):
    '''given a polyomino, return a list of polyominos in canonical form
    with one additional adjacent piece added.
    '''

    l_next = []
    for tup in s_tuple:
        # for each point in the polyomino, compute a new adjacent point
        # and add it to the polyomino
        l_points = [ (tup[0], tup[1] + 1),   # up
                     (tup[0], tup[1] - 1),   # down
                     (tup[0] + 1, tup[1]),   # left
                     (tup[0] - 1, tup[1]) ]  # right

        for point in l_points:
            s_temp = set(s_tuple)
            if point not in s_tuple:
                s_temp.add( point )
                l_next.append( canonicalize(s_temp) )
    return l_next


def rotate90( s_tuple ):
    return canonicalize( [ (-tup[1], tup[0]) for tup in s_tuple ] )

def rotate180( s_tuple ):
    return canonicalize( rotate90( rotate90( s_tuple ) ) )

def rotate270( s_tuple ):
    return canonicalize( rotate90( rotate180( s_tuple ) ) )

def computeNext( l_polyomino ):
    l_poly_next = []
    for p in l_polyomino:
        for p_next in addOne( p ):
            if not(p_next in l_poly_next) and \
               not(rotate90(p_next) in l_poly_next) and \
               not(rotate180(p_next) in l_poly_next) and \
               not(rotate270(p_next) in l_poly_next):
                l_poly_next.append( p_next )
    return l_poly_next


def display2(x):
    display(x)
    print ''

l_p = {}
l_p[1] = [[(0,0)]]

for i in range(1,9):
    l_p[i+1] = computeNext( l_p[i] )
    print '%d:\t%d' % (i+1, len(l_p[i+1]) )


map( display2, l_p[8] )

