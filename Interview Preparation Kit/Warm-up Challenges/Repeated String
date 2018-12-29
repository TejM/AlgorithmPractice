""" https://www.hackerrank.com/challenges/repeated-string """

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num_a_in_string = 0
    for x in s:
        if x == 'a':
            num_a_in_string += 1
         
    num_a = num_a_in_string * (n//len(s))

    for y in range (n%len(s)):
        if s[y]== 'a':
            num_a += 1
    return num_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
