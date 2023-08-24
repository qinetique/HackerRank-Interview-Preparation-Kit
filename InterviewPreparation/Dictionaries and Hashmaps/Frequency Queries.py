# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Frequency Queries
# Sub-Domain : Interview Preparation kit | Dictionaries and Hashmaps
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/frequency-queries/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    c = dict()
    r = list()
    for i in queries:
        if i[0] == 1:
            try:
                c[i[1]] += 1
            except:
                c[i[1]] = 1
        elif i[0] == 2:
            try:
                c[i[1]] -= 1
                if c[i[1]] == 0:
                    del c[i[1]]
            except:
                continue
        elif i[0] == 3:
            if i[1] in set(c.values()):
                r.append('1')
            else:
                r.append('0')
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
