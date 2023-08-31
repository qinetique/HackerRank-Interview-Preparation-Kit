# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Roads and Libraries
# Sub-Domain : Interview Preparation kit | Graphs
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
import sys


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road > c_lib:
        return c_lib * n
    c = 0
    g = {}
    for i in cities:
        u, v = i
        if u not in g:
            g.update({u: []})
        if v not in g:
            g.update({v: []})
        g[v].append(u)
        g[u].append(v)
    vst = {k: False for k in g}
    if len(g) < n:
        c += (n - len(g)) * c_lib
    for nd in g:
        if not vst[nd]:
            vst[nd] = True
            c += c_lib
            c += building(nd, g, vst, c_road)
    return c


def building(nd, g, vst, c_road):
    c = 0
    for another_nd in g[nd]:
        if not vst[another_nd]:
            vst[another_nd] = True
            c += c_road
            c += building(another_nd, g, vst, c_road)
    return c


if __name__ == '__main__':
    fptr = sys.stdout
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        c_lib = int(first_multiple_input[2])
        c_road = int(first_multiple_input[3])
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        fptr.write(str(result) + '\n')
    fptr.close()
