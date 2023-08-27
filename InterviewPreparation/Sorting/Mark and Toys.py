# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Mark and Toys
# Sub-Domain : Interview Preparation kit | Sorting
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    price = 0
    item = 0
    prices.sort()
    for i in range(0, n):
        if price + prices[i] < k:
            price += prices[i]
            item += 1
    return item


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
