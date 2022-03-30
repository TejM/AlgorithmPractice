""" https://www.hackerrank.com/challenges/migratory-birds/ """
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    
    #1st part is to collect 2d array of ID number and number of occurances.
    
    array = [[None,0]]
    for x in arr:
        y = 0
        a = True
        while a and y < len(array):
            if x == array[y][0]:
                array[y][1] += 1
                a = False
            y += 1 
        if y == len(array) and a:    
            array.append([x,1])
            
    # 2nd part is to collect the highest number of occurances        
    maxVal = 0
    for z in range(len(array)):
        if array[z][1] > maxVal:
            maxVal = array[z][1]
    #3rd part is to relate highest occurance to ID number and choose the smallest in case of repeat.
    
    arrayID = []
    
    for i in range(len(array)):
        if array[i][1] == maxVal:
            arrayID.append(array[i][0])
    return min(arrayID)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
