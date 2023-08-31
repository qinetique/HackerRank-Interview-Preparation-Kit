# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Find the nearest clone
# Sub-Domain : Interview Preparation kit | Graphs
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
import sys
from queue import Queue


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = {}
    for i, j in zip(graph_from, graph_to):
        if not i in graph:
            graph.update({i: {'near': [], 'color': ids[i - 1]}})
        if not j in graph:
            graph.update({j: {'near': [], 'color': ids[j - 1]}})
        graph[i]['near'].append(j)
        graph[j]['near'].append(i)
    sum_displacement = -1
    for k in graph:
        if graph[k]['color'] == val:
            short_dis = function_queue(graph, k, graph[k]['color'])
            if short_dis < sum_displacement or sum_displacement == -1:
                sum_displacement = short_dis
    return sum_displacement


def function_queue(graph, node, color):
    q = Queue()
    q.put(node)
    ck = {b: False for b in graph}
    ck[node] = True
    d = 0
    while not q.empty():
        node = q.get()
        d += 1
        for sec_node in graph[node]['near']:
            if not ck[sec_node]:
                ck[sec_node] = True
                q.put(sec_node)
                if graph[sec_node]['color'] == color:
                    return d
    return -1


if __name__ == '__main__':
    fptr = sys.stdout
    graph_nodes, graph_edges = map(int, input().split())
    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges
    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())
    ids = list(map(int, input().rstrip().split()))
    val = int(input())
    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    fptr.write(str(ans) + '\n')
    fptr.close()
