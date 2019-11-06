#https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s.split(" "))
    words = []
    for name in s:
        if (name == ''):
            words.append(name)
            continue
        elif (name[0].islower()):
            words.append (name[0].upper() + name[1:])
        else: 
            words.append(name)
    return(" ".join(words))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
