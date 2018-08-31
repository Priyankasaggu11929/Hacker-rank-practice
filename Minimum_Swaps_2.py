#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    minswap=0
    i=0
    arr2=sorted(arr)
    while i<len(arr):
        if arr==arr2:
            break
        if arr[i]==i+1:
            i+=1
            continue
        arr[arr[i]-1], arr[i]=arr[i], arr[arr[i]-1]
        minswap+=1
    return minswap    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
