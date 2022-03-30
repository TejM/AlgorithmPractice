""" https://www.hackerrank.com/challenges/time-conversion/problem """

#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    if (s[-2:] == 'PM' and s[0:2] != '12'):
        hh = int(s[0:2])
        hh = hh + 12
        return str(hh) + s[2:-2]
    if (s[-2:] == 'AM' and s[0:2] == '12'):
        hh = '00'
        return hh + s[2:-2]
    else:
        return s[:-2]
        
    
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
