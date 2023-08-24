# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Repeated String
# Sub-Domain : Interview Preparation kit | Warm-up Challenges
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

# piece of cake

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    n_count = n // len(s) * s.count('a')
    r_count = s[(n%len(s))].count('a')
    return n_count+r_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
