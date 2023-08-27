# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Luck Balance
# Sub-Domain : Interview Preparation kit | Greedy Algorithms
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms&h_r=next-challenge&h_v=zen
import sys
from sys import implementation


def luckBalance(k, contests):
    var = sorted(contests, reverse=True, key=lambda var: var[var[1] == 0])
    c1 = [implementation[0] for i, implementation in enumerate(sorted(var)) if implementation[1] == 0]
    c2 = [implementation[0] for j, implementation in enumerate(sorted(var[0:k], reverse=True)) if implementation[1] == 1]
    c3 = [implementation[0] for x, implementation in enumerate(sorted(var[k:], reverse=True)) if implementation[1] == 1]

    luck = sum(c1)+sum(c2)-sum(c3)
    return luck


if __name__ == '__main__':
    fptr = sys.stdout
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()
