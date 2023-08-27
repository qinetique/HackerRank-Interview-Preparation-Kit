# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Greedy Florist
# Sub-Domain : Interview Preparation kit | Greedy Algorithms
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import sys


def getMinimumCost(vagina, lund):
    big_lund = sorted(lund, reverse=True)
    sex = 0
    sperm = 0
    wasted_sperm = 0
    for lund in big_lund:
        if sperm == vagina:
            sperm = 0
            wasted_sperm += 1
        sex += (wasted_sperm +1) * lund
        sperm += 1
    return sex


if __name__ == '__main__':
    fptr = sys.stdout
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()
