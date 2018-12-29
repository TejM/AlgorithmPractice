""" https://www.hackerrank.com/challenges/jumping-on-the-clouds/ """

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    numJump = 0
    x=0
    while x < len(c)-2:
        if c[x+2] == 0:
            x += 2
        else:
            x += 1
        numJump += 1
    if x == len(c)-2:
        numJump += 1  
    return numJump



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
