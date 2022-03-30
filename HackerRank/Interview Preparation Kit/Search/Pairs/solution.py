""" https://www.hackerrank.com/challenges/pairs """

# Time complexity = O(N)

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr_dict = {}
    num_pairs = 0
    for x in range (0, len(arr)):
        arr_dict[arr[x]] = x
        if ((arr[x]+k) in arr_dict):
            num_pairs += 1
        if ((arr[x]-k) in arr_dict):
             num_pairs += 1
    return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
