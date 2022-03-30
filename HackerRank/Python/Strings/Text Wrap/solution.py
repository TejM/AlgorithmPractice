#https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    x = 0
    lyst =[]
    while(x < len(string)): 
        lyst.append(string[x:x+max_width])
        x = x + max_width
    return "\n".join(lyst)

if __name__ == '__main__':
