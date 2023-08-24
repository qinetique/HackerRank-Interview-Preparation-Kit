# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Sherlock and Anagrams
# Sub-Domain : Interview Preparation kit | Dictionaries and Hashmaps
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    n = len(s)
    ss = {}
    ang = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            myjoin = ''.join(sorted(s[i:j]))
            if myjoin in ss:
                ss[myjoin] += 1
            else:
                ss[myjoin] = 1
    for i in ss:
        n = ss[i] - 1
        ang += ((n * (n + 1)) // 2)
    return ang


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()
