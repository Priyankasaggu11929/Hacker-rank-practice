#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    count=0
    for item in note:
        if item in magazine:
            magazine.remove(item)
            count+=1
            continue
        else:
            print("No")
            break

    if count==len(note):
        print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
