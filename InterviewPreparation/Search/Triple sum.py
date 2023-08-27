# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Triple sum
# Sub-Domain : Interview Preparation kit | Search
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/triple-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import sys


def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    x, y, z = 0, 0, 0
    solution = 0
    while y < len(b):
        while x < len(a) and a[x] <= b[y]:
            x += 1
        while z < len(c) and c[z] <= b[y]:
            z += 1
        solution += x * z
        y += 1
    return solution


if __name__ == '__main__':
    fptr = sys.stdout
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    fptr.write(str(ans) + '\n')
    fptr.close()
