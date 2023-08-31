# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : BFS: Shortest Reach in a Graph
# Sub-Domain : Interview Preparation kit | Graphs
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

from heapq import heappush, heappop, heapify, heappushpop, heapreplace


class Graph:
    def __init__(self, node_length):
        self.edges = [[] for _ in range(node_length)]
        self.length = node_length
        self.distance = [-1] * node_length
        self.heap = []

    def connect(self, src, target):
        self.edges[src].append(target)
        self.edges[target].append(src)

    def min_distance(self, src, side_node, v):
        src_distance = self.distance[src] if self.distance[src] > 0 else 0
        for node in side_node:
            if not v[node]:
                new_distance = src_distance + 6
                current_distance = self.distance[node]
                if current_distance == -1 or current_distance > new_distance:
                    self.distance[node] = new_distance
                    heappush(self.heap, (new_distance, node))
        if len(self.heap) > 0:
            return heappop(self.heap)
        else:
            return (None, None)

    def find_all_distances(self, src, past_v):
        new_v = past_v[:]
        new_v[src] = True
        side_node = self.edges[src]
        _, next_node = self.min_distance(src, side_node, past_v)
        if next_node != None:
            self.find_all_distances(next_node, new_v)

    def to_print(self, src):
        del self.distance[src]
        unreachable_node = map(str, self.distance)
        print(' '.join(unreachable_node))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1, [False] * n)
    graph.to_print(s - 1)
