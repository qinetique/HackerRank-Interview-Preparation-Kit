# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Max Min
# Sub-Domain : Interview Preparation kit | Greedy Algorithms
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/angry-children/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import sys


def maxMin(k, arr):
    array_sort = sorted(arr)
    min_u = array_sort[k - 1] - array_sort[0]
    for i in range(1, len(array_sort) - k + 1):
        u = array_sort[i + k - 1] - array_sort[i]
        if min_u > u:
            min_u = u
    return min_u


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
