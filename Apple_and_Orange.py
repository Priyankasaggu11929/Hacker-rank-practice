#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    noa,noo=0,0
    for i in range(len(apples)):
        apples[i]+=a
    for j in range(len(oranges)):
        oranges[j]+=b
    for apple in apples:
        if s<=apple<=t:
            noa+=1
        else:
            continue
    for orange in oranges:
        if s<=orange<=t:
            noo+=1
        else:
            continue
    return print("{}\n{}".format(noa,noo))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
