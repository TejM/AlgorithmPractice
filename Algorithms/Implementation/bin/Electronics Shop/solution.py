#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the getMoneySpent function below.
# 

""" The brute force method: (More efficient method implemented in the actual function)

time complexity: O(n*m)
space complexity O(1)

maxTotal = -1
    for i in keyboards:
        for j in drives:
            total = i + j  
            if (total > maxTotal) and (total <= b) :
                maxTotal = total
    return maxTotal

"""

"""Soring the lists and then working with them is a better option. Python's inbuilt sort is Timsort, which is O(nlogn). """


def getMoneySpent(keyboards, drives, b):
    
    max = -1
    keyboards.sort()
    drives.sort()
    for i in keyboards:
        for j in drives:
            if (i+j) > b:
                break
            if (i+j) > max:
                max = i+j
    return max                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = raw_input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = map(int, raw_input().rstrip().split())

    drives = map(int, raw_input().rstrip().split())

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
