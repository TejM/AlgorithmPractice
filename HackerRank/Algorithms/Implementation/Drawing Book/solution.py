""" https://www.hackerrank.com/challenges/drawing-book """

#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if (p <= n/2):
        return str (p//2)
    else: 
        if n % 2 == 0:
            return str ((n - p + 1)//2)
        else:     
            return str ((n - p)//2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    p = int(raw_input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
