#!usr/bin/env python3

import sys

N=int(input())
word=list(input().rstrip())

pre=[]
po=[]


def fMI(lis, l, h):
    if l>h:
        return sys.maxsize
    if l==h:
        return 0
    if l==h-1:
        return (0 if lis[l]==lis[h] else 1)

    return (fMI(lis, l + 1, h - 1) if lis[l]==lis[h] else (min(fMI(lis, l, h - 1),fMI(lis, l + 1, h)) + 1))

print(fMI(word, 0, len(word)-1))
