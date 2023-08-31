# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Candies
# Sub-Domain : Interview Preparation kit | Dynamic Programming
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/max-array-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
import sys


def candies(n, arr):
    c = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            c[i] = c[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1] and c[i] <=c[i+1]:
            c[i] = c[i + 1] + 1
    return sum(c)


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = candies(n, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
