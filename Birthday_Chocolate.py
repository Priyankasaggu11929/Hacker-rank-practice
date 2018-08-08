#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count=0
    i=0
    while i<n:
        if len(s)-i>=m:
            sum=0
            for j in range(m):
                temp=j
                temp=temp+i
                sum+=s[temp]
        else:
            break
        if sum==d:
            count+=1
            i+=1
        else:
            i+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
