#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    i,j,k=0,0,0
    test1,test2,test3=[],[],[]
    for i in range(4):
        for k in range(6):
            sum=0
            if (k+3)<=6:
                for j in range(k,k+3):
                    sum+=arr[i][j]
                test1.append(sum)
    for i in range(1,5):
        for j in range(1,5):
            test2.append(arr[i][j])
    for i in range(2,6):
        for k in range(6):
            sum=0
            if (k+3)<=6:
                for j in range(k,k+3):
                    sum+=arr[i][j]
                test3.append(sum)

    for i in range(16):
        test1[i]=test1[i]+test2[i]+test3[i]
    return max(test1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    
    fptr.write(str(result) + '\n')

    fptr.close()
