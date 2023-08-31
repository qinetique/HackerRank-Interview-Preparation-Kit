# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Dynamic Programming
# Sub-Domain : Interview Preparation kit | Dynamic Programming
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/max-array-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
import sys


def abbreviation(a, b):
    n, m = len(a), len(b)
    dhon = [[False] * (m + 1) for _ in range(n + 1)]

    dhon[0][0] = True
    for i in range(1, n + 1):
        dhon[i][0] = a[:i].islower()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1].isupper():
                if a[i - 1] == b[j - 1]:
                    dhon[i][j] = dhon[i - 1][j - 1]
                else:
                    dhon[i][j] = False
            else:
                if a[i - 1].upper() == b[j - 1]:
                    dhon[i][j] = dhon[i - 1][j] or dhon[i - 1][j - 1]
                else:
                    dhon[i][j] = dhon[i - 1][j]

    if dhon[n][m]:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = sys.stdout
    q = int(input().strip())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        fptr.write(result + '\n')
    fptr.close()
