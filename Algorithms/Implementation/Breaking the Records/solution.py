""" https://www.hackerrank.com/challenges/breaking-best-and-worst-records """

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    
    bestScore, worstScore = scores[0], scores[0]
    numBreakRecord = [0,0]
    
    for i in scores[1:]:
        if i > bestScore:
            bestScore = i
            numBreakRecord[0] += 1
        if i < worstScore:
            worstScore = i
            numBreakRecord[1] += 1
    return (numBreakRecord)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
