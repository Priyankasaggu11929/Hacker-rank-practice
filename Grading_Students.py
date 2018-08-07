#!/bin/python3
#Day-3 Problem3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    final=[]
    for i in range(len(grades)):
        if grades[i]>37:
            x=grades[i]%5
            if (5-x)<3:
                grades[i]+=(5-x)
                final.append(grades[i])
            else:
                final.append(grades[i])
        else:
            final.append(grades[i])
    return final

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
    
    print(grades)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

