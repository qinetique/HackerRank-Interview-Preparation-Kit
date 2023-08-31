# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Dynamic Programming
# Sub-Domain : Interview Preparation kit | Dynamic Programming
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/max-array-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
import sys


def maxSubsetSum(arr):
    x = [0] * len(arr)
    x[0], x[1] = arr[0], max([arr[0], arr[1]])
    for i in range(n):
        x[i] = max(x[i - 1], x[i - 2] + arr[i])
    return x[-1]


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
