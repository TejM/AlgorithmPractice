"""https://www.hackerrank.com/challenges/counting-valleys"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height, numValleys = 0,0
    for i in s:
        if i == 'D':
            height -= 1
        else:
            if height == -1:
              numValleys += 1
            height += 1
    return numValleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
