# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Alternating Characters
# Sub-Domain : Interview Preparation kit | String Manipulation
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# change this 's' to SEX
def alternatingCharacters(sex):
    dhon = 0
    for i in range(1, len(sex)):
        if sex[i] == sex[i - 1]:
            dhon += 1
    return dhon


if __name__ == '__main__':
    fptr = sys.stdout
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()
