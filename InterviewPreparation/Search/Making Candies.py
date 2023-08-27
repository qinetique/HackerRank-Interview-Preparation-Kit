# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Making Candies
# Sub-Domain : Interview Preparation kit | Search
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/making-candies/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search
import math
import sys


def minimumPasses(m, w, p, n):
    d = 0
    c = 0
    solve = math.ceil(n / (m * w))
    while solve > d:
        if p > c:
            nd = math.ceil((p - c) / (m * w))
            c += nd * m * w
            d += nd
        sub = abs(m - w)
        a = c // p
        pd = min(sub, a)
        if m < w:
            m += pd
        else:
            w += pd
        r = a - pd
        m += r // 2
        w += r - r // 2
        c -= a * p
        c += m * w
        d += 1
        car = max(n - c, 0)
        x = math.ceil(car / (m * w))
        solve = min(solve, d + x)
    return solve


if __name__ == '__main__':
    fptr = sys.stdout
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    w = int(first_multiple_input[1])
    p = int(first_multiple_input[2])
    n = int(first_multiple_input[3])
    result = minimumPasses(m, w, p, n)
    fptr.write(str(result) + '\n')
    fptr.close()
