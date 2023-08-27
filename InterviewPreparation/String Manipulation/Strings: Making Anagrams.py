# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Strings: Making Anagrams
# Sub-Domain : Interview Preparation kit | String Manipulation
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    x = Counter(a)
    y = Counter(b)
    dif_a = x - y
    dif_b = y - x
    return sum(dif_a.values()) + sum(dif_b.values())


if __name__ == '__main__':
    fptr = sys.stdout
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
