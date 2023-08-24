# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Hash Tables: Ransom Note
# Sub-Domain : Interview Preparation kit | Dictionaries and Hashmaps
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()
    for i in note:
        if i not in magazine:
            b = False
            break
        else:
            magazine.remove(i)
        b = True
    if b:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
