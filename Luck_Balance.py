#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    one=[]
    zero=[]
    temp=0
    for elements in contests:
        if elements[1]==1:
            one.append(elements[0])
        else:
            zero.append(elements[0])
    x=sorted(one)
    for i in range(len(x)-k):
        temp+=x[i]
        x[i]=0
    return (sum(x)+sum(zero)-temp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])
    print(n)

    k = int(nk[1])
    print(k)
    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    
    print(contests)
        
    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()

