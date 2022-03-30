"""https://www.hackerrank.com/challenges/ctci-recursive-staircase"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    ways_to_climb = [0, 1, 2, 4]
    
    for num_stairs in range(4, n+1):
        ways_to_climb.append(ways_to_climb[num_stairs-3] +ways_to_climb[num_stairs-2]+ ways_to_climb[num_stairs-1] ) 
    return(ways_to_climb[n])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
