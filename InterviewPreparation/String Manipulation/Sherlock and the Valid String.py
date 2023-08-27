# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Sherlock and the Valid String
# Sub-Domain : Interview Preparation kit | String Manipulation
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(sex):
    handling = {}
    for dhon in sex:
        handling.setdefault(dhon, 0)
        handling[dhon] += 1
    gud = list(handling.values())
    virginity = gud[0]  # still intake
    dhon_gud_relation = 0

    for sperm in gud:
        sperm_count = abs(sperm - virginity)
        dhon_gud_relation += sperm_count if sperm != 1 else 1
        if dhon_gud_relation > 1:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
