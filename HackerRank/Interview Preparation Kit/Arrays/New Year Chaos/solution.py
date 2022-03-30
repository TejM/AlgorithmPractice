""" https://www.hackerrank.com/challenges/new-year-chaos """

# This is a naive solution. While it has a single for loop (and hence is O(N)), it requires unneccessary swaps. 
# Solution with simple counting should ofcourse be possible, I will implement that later. 

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    

    total_bribes = 0
    
    for x in range (len(q)-1, 0, -1):
        if (q[x] != x+1):
            y = 1
            while (q[x-y] != x+1):
                y = y + 1
                if (y == 3):
                    print ("Too chaotic")
                    return
            if (y == 1):
                temp1 = q[x]
                q[x] = q[x-y]
                q[x-y] = temp1
                total_bribes = total_bribes + 1
            elif (y==2):
                temp1 = q[x]
                q[x] = q[x-y]
                q[x-y] = temp1
                
                temp2 = q[x-y+1]
                q[x-y+1] = q[x-y]
                q[x-y] = temp2
                total_bribes = total_bribes + 2           
    print (total_bribes)
            

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
