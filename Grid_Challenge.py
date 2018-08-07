#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    flag=0
    new=[]
    for elements in grid:
        y=list(elements)
        x=sorted(y)
        new.append(x)
    b = [[new[j][i] for j in range(len(new))] for i in range(len(new[0]))]
    for item in b:
        c=sorted(item)
        if c==item:
            flag=1
            continue
        else:
            flag=0
            break
    if flag==1:
        return "YES"
    else:
        return "NO"

                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

