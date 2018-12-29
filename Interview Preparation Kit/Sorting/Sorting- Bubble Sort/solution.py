""" https://www.hackerrank.com/challenges/ctci-bubble-sort """

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numSwap = 0
    for x in range (0, len(a)):
        for y in range (0, len(a)-1):
            if a[y] > a[y+1]:
                temp = a[y]
                a[y]= a[y+1]
                a[y+1] = temp
                numSwap += 1  

    print ("Array is sorted in", numSwap ,"swaps.")
    print ("First Element:", a[0])
    print ("Last Element:", a[len(a) -1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
