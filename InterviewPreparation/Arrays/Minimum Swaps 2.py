# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Minimum Swaps 2
# Sub-Domain : Interview Preparation kit | Arrays
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    total = 0
    s = 0
    while s < len(arr):
        if arr[s] == s + 1:
            s += 1
            continue
        arr[arr[s] - 1], arr[s] = arr[s], arr[arr[s] - 1]
        total += 1
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()