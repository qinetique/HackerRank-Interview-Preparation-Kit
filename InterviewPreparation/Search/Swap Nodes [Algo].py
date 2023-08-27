# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Swap Nodes [Algo]
# Sub-Domain : Interview Preparation kit | Search
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

# run this in Pypy3 to avoid runtime error

import sys


def swapNodes(indexes, queries):
    sys.setrecursionlimit(1024 * 2)
    for i in queries:
        solution = []

        def defsalgo(nd, dp):
            if nd == - 1:
                return None
            cnode = indexes[nd - 1]
            if dp % i == 0:
                cnode[0], cnode[1] = cnode[1], cnode[0]
            defsalgo(cnode[0], dp + 1)
            solution.append(nd)
            defsalgo(cnode[1], dp + 1)

        defsalgo(1, 1)
        yield solution


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = swapNodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()
