""" https://www.hackerrank.com/challenges/the-birthday-bar """

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    
    count = 0 # number of times squares of segment add up to the value of day
    for x in range(len(s)-m+1):
        total = 0  # Sum of the square of chosen segment 
        for y in range (m):
            total += s[x+y]
        if total == d:
            count += 1
    return (count)                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    s = map(int, raw_input().rstrip().split())

    dm = raw_input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
