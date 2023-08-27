# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Minimum Absolute Difference in an Array
# Sub-Domain : Interview Preparation kit | Greedy Algorithms
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr.sort()
    dif = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < dif:
            dif = abs(arr[i] - arr[i + 1])
    return dif


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
