""" https://www.hackerrank.com/challenges/sock-merchant """

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    
    currentVal = ar[0]
    curentValRun = 0
    i = 0
    numPairs = 0
    while i < n:
        if ar[i] == currentVal:
            curentValRun += 1
            if i + 1 == n:
                numPairs += (curentValRun // 2)           
        else: 
            numPairs += (curentValRun // 2)
            currentVal = ar[i]
            curentValRun = 1  
        i += 1
    return numPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
