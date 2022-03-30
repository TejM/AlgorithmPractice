"""https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/"""

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):

    cost_dict ={}
    for index, num in enumerate(cost):
        remain = money - num
        if remain not in cost_dict:
            cost_dict[num] = index
        else:
            print (cost_dict[remain]+1, index+1)

      
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
