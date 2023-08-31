# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Min Max Riddle
# Sub-Domain : Interview Preparation kit | Stacks and Queues
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
import sys
from collections import defaultdict


def riddle(arr):
    arr.append(-1)
    solution = [0] * (len(arr) - 1)
    d, s = defaultdict(int), []
    for i, j in enumerate(arr):
        ix = i
        while s and s[-1][0] >= j:
            k, ix = s.pop()
            d[i - ix] = max(d[i - ix], k)
        s.append((j, ix))
    c = 0

    for x in range(len(arr) - 1, 0, -1):
        c = max(c, d[x])
        solution[x - 1] = c
    return solution


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = riddle(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
