# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Roads and Libraries
# Sub-Domain : Interview Preparation kit | Graphs
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
import sys
from collections import defaultdict


def minTime(roads, machines):
    p = {}
    dd = defaultdict(int)
    for i in machines:
        dd[i] = 1
    search = lambda node: node if p.get(node, node) == node else search(p[node])

    def dontknowthefunction(i, j):
        u, v = search(i), search(j)
        if not dd[u] or not dd[v]:
            if i != u:
                u, v = v, u
            p[u] = v
            dd[u] |= dd[v]
            dd[v] |= dd[u]
            return True
    return sum(k for i, j, k in sorted(roads, key=lambda i: -i[2]) if not dontknowthefunction(i, j))


if __name__ == '__main__':
    fptr = sys.stdout
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    roads = []
    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))
    machines = []
    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)
    result = minTime(roads, machines)
    fptr.write(str(result) + '\n')
    fptr.close()
