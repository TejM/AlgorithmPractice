""" https://www.hackerrank.com/challenges/grading/problem """

#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i in range(len(grades)): https://github.com/TejM/HackerRank-Solutions
        x = grades[i]
        if x % 5 > 2 and x > 37:
            x = (x + 5) - (x%5)
        grades[i] = x
    return grades
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
