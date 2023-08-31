# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Recursion: Davis' Staircase
# Sub-Domain : Interview Preparation kit | Recursion and Backtracking
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking
import sys


def stepPerms(n):
    module_value = 10**10 + 7
    v = [0] * max(3, n + 1)
    v[0] = 1
    v[1] = 1
    v[2] = v[1] + v[0]
    for i in range(3, n + 1):
        v[i] = (v[i - 1] + v[i - 2] + v[i - 3]) % module_value
    return v[n]


if __name__ == '__main__':
    fptr = sys.stdout
    s = int(input().strip())
    for s_itr in range(s):
        n = int(input().strip())
        res = stepPerms(n)
        fptr.write(str(res) + '\n')
    fptr.close()
