# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Count Triplets
# Sub-Domain : Interview Preparation kit | Dictionaries and Hashmaps
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/count-triplets-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# !/bin/python3

import math
import os
import random
import re
import sys
import collections


# Complete the countTriplets function below.
def countTriplets(arr, r):
    arrx = collections.defaultdict(int)
    arry = collections.defaultdict(int)
    c = 0
    for i in arr:
        c += arry[i]
        arry[i * r] += arrx[i]
        arrx[i * r] += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
