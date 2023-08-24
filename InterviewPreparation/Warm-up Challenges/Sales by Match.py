# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Sales by Match
# Sub-Domain : Interview Preparation kit | Warm-up Challenges
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    p = 0
    v = []
    for i in range(n):
        if ar[i] not in v:
            v.append(ar[i])
            c = 1
            for j in range(i + 1, n):
                if ar[i] == ar[j]:
                    c += 1
            p += c // 2
    return p


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
