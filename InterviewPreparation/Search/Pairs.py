# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Pairs
# Sub-Domain : Interview Preparation kit | Search
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search
import sys


def pairs(k, arr):
    arr.sort()
    l = 0
    r = 0
    solve = 0
    while r < len(arr):
        v = arr[r] - arr[l]
        if v == k:
            solve += 1
            l += 1
            r += 1
        elif v < k:
            r += 1
        else:
            l += 1
            if v == k:
                r += 1
    return solve


if __name__ == '__main__':
    fptr = sys.stdout
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
