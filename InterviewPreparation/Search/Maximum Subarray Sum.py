# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Maximum Subarray Sum
# Sub-Domain : Interview Preparation kit | Search
# Domain : HackerRank
# Problem URL : hackerrank.com/challenges/maximum-subarray-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search
import sys
from bisect import bisect, insort


def maximumSum(a, m):
    ro_sum = 0
    c_sum = []
    maximum = 0
    for i in range(len(a)):
        ro_sum = (ro_sum + a[i]) % m
        cen = bisect(c_sum, ro_sum)
        d = 0 if cen == i else c_sum[cen]
        maximum = max(maximum, (ro_sum+m-d) % m)
        insort(c_sum, ro_sum)
    return maximum


if __name__ == '__main__':
    fptr = sys.stdout
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))
        result = maximumSum(a, m)
        fptr.write(str(result) + '\n')
    fptr.close()
