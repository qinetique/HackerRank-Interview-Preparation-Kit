# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Fraudulent Activity Notifications
# Sub-Domain : Interview Preparation kit | Sorting
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    c = 0
    ac = [0] * 201
    for i in range(d):
        ac[expenditure[i]] += 1
    for i in range(d, len(expenditure)):
        if expenditure[i] >= mvalue(ac, d) * 2:
            c += 1
        ac[expenditure[i - d]] -= 1
        ac[expenditure[i]] += 1
    return c


def mvalue(c_arr, d):
    elen = d % 2 == 0
    total = 0
    for i, c in enumerate(c_arr):
        total += c
        if elen:
            if total == d // 2:
                for j in range(i + 1, len(c_arr)):
                    if c_arr[j] > 0:
                        return (i + j) / 2
            elif total > d // 2:
                return i
        else:
            if total >= d // 2 + 1:
                return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    fptr.write(str(result) + '\n')
    fptr.close()
