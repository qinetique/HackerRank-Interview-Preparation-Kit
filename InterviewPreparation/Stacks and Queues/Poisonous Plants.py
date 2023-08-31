# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Poisonous Plants
# Sub-Domain : Interview Preparation kit | Stacks and Queues
# Domain : HackerRank
# Problem URL :
# https://www.hackerrank.com/challenges/poisonous-plants/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

import sys


def poisonousPlants(p):
    solution = 0
    s = []
    for i, j in enumerate(p):
        d = 1
        while s and s[-1][0] >= j:
            d = max(d, s[-1][1] + 1)
            s.pop()
        if not s:
            d -= 1
        solution = max(solution, d)
        s.append((j, d))
    return solution


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = poisonousPlants(p)
    fptr.write(str(result) + '\n')
    fptr.close()
