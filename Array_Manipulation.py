#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate

# Complete the arrayManipulation function below.
def arrayManipulation(n):
    arr=[0]*(n+1)
    for _ in range(m):
        a,b,c=map(int, input().split(' '))
        arr[a-1]+=c
        arr[b]-=c
    return(max(accumulate(arr)))
    
        
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    

    result = arrayManipulation(n)

    fptr.write(str(result) + '\n')

    fptr.close()
