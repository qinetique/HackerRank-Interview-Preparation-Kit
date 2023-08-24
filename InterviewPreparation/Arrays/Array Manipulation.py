# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Array Manipulation
# Sub-Domain : Interview Preparation kit | Arrays
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    mv = 0
    total = 0
    arr = [0] * (n + 1)
    for i in queries:
        l = i[0]
        r = i[1]
        s = i[2]
        arr[l - 1] += s
        arr[r] -= s
    for j in arr:
        total += j
        mv = max(mv, total)
    return mv


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
