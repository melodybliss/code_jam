#!/usr/bin/env python
#T9 spelling

import sys

t9_dict = {
    1   :       '1',
    2   :	'ABC2',
    3   :       'DEF3',
    4   :       'GHI4',
    5   :       'JKL5',
    6   :       'MNO6',
    7   :       'PQRS7',
    8   :       'TUV8',
    9   :       'WXYZ9',
    0   :	' 0'
}

def get_key(c):
    c = c.upper()
    for num in t9_dict:
        loc = t9_dict[num].find(c)
        if loc != -1:
            return str(num) * (loc+1)

def print_seq(seq):
    r=''
    last=''
    for i in seq:
        if i[0] == last:
            r = r + ' '
        r = r + i
        last=i[0]
    return r

case=1
for line in sys.stdin:
    if case > 100:
        exit
    keypress=[]
    #print "LINE:", line,
    for c in line:
        key = get_key(c)
        if key != None:
            keypress.append(key)

    print 'Case #' + str(case) + ": " + print_seq(keypress)
    case += 1
