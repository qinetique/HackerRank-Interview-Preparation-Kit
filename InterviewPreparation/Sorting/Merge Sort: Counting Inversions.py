# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Merge Sort: Counting Inversions
# Sub-Domain : Interview Preparation kit | Sorting
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-merge-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mg(arr, l, m, r):
    if arr[m] <= arr[m + 1]:
        return 0
    c = 0
    lt = arr[l:m + 1]
    rt = arr[m + 1:r + 1]
    x = 0
    y = 0
    done = l
    len_l = m + 1 - l
    len_r = r - m
    while x < len_l and y < len_r:
        if lt[x] <= rt[y]:
            arr[done] = lt[x]
            x += 1
        else:
            arr[done] = rt[y]
            y += 1
            c += len_l - x
        done += 1
    arr[done:done + len_l - x] = lt[x:]
    return c


def sort_mg(arr, l, r):
    p = 0
    if l < r:
        m = (l + r) // 2
        p = sort_mg(arr, l, m)
        p += sort_mg(arr, m + 1, r)
        p += mg(arr, l, m, r)

    return p


def countInversions(arr):
    p = sort_mg(arr, 0, len(arr) - 1)
    return p


if __name__ == '__main__':
    fptr = sys.stdout
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        fptr.write(str(result) + '\n')
    fptr.close()
