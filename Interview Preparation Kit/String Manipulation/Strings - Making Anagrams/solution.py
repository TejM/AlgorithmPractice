""" https://www.hackerrank.com/challenges/ctci-making-anagrams """

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    countArray1 = [0]*26
    countArray2 = [0]*26
    
    for i in range(0,len(a)):
       countArray1[ord(a[i]) - ord('a')] += 1
       i += 1

    for j in range (0,len(b)):
        countArray2[ord(b[j])-ord('a')] += 1
        j += 1

    numDelete = 0
    for k in range (0,26):
        numDelete += abs(countArray1[k] - countArray2[k])
    return numDelete

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
