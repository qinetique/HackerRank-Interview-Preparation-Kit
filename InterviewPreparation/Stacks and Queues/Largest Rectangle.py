# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Largest Rectangle
# Sub-Domain : Interview Preparation kit | Stacks and Queues
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
import sys


def largestRectangle(h):
    s = list()
    i = 0
    l_rec = 0
    while i < len(h):
        if not s or h[s[-1]] <= h[i]:
            s.append(i)
            i += 1
        else:
            top = s.pop()
            area = (h[top] * ((i - s[-1] - 1) if s else i))
            l_rec = max(l_rec, area)
    while s:
        top = s.pop()
        area = (h[top] * ((i - s[-1] - 1) if s else i))
        l_rec = max(l_rec, area)
    return l_rec


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    h = list(map(int, input().rstrip().split()))
    result = largestRectangle(h)
    fptr.write(str(result) + '\n')
    fptr.close()
