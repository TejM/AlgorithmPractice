""" https://www.hackerrank.com/challenges/day-of-the-programmer/ """

#!/bin/python
import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.

def dayOfProgrammer(year):
    isLeap = False
    
    if (year<1918): 
        if (year%4 == 0):
            isLeap = True
        if (isLeap):    
            s='12.09.' + str(year)  
        else:
            s='13.09.' + str(year)     
    
    if (year == 1918):
        s='26.09.' + str(year)  
        
    if (year>1918):    
    
        if ((year % 400 == 0) or ((year % 4 == 0) and  (year % 100 != 0))):
            isLeap = True
        if isLeap:
            s='12.09.' + str(year)  
        else: 
            s='13.09.' + str(year)     
        
    return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(raw_input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
