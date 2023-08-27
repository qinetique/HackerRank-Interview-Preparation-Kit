# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Sorting
# Sub-Domain : Interview Preparation kit | Sorting
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    c = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                a[i] = a[i] + a[j]
                a[j] = a[i] - a[j]
                a[i] = a[i] - a[j]
                c += 1
    print('Array is sorted in {} swaps.'.format(c))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
