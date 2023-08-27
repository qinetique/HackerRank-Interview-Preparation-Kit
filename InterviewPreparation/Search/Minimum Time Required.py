# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Minimum Time Required
# Sub-Domain : Interview Preparation kit | Search
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search
import math
import sys


def minTime(machines, goal):
    machines, c = sorted(machines), len(machines)
    minimum = math.ceil(goal / c) * machines[0]
    maximum = math.ceil(goal / c) * machines[-1]
    while maximum > minimum:
        d = (maximum + minimum) // 2
        sum_d = sum(d // i for i in machines)
        if sum_d >= goal:
            maximum = d
        else:
            minimum = d + 1
    return minimum


if __name__ == '__main__':
    fptr = sys.stdout
    nGoal = input().split()
    n = int(nGoal[0])
    goal = int(nGoal[1])
    machines = list(map(int, input().rstrip().split()))
    ans = minTime(machines, goal)
    fptr.write(str(ans) + '\n')
    fptr.close()
