# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Flipping bits
# Sub-Domain : Interview Preparation kit | Miscellaneous
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous
import sys


def flippingBits(n):
    # Write your code here

if __name__ == '__main__':
    fptr = sys.stdout
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
