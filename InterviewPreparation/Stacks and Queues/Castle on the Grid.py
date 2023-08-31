# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Castle on the Grid
# Sub-Domain : Interview Preparation kit | Stacks and Queues
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
import sys
from collections import deque


def minimumMoves(g, startX, startY, goalX, goalY):
    def next(g, p, q, v):
        r, c = len(g), len(g[-1])
        cx, cy, cs = p
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx, cy
            while True:
                nx, ny = nx + dx, ny + dy
                if r > nx >= 0 and c > ny >= 0 and g[nx][ny] != 'X':
                    if (nx, ny) not in v:
                        v.add((nx, ny))
                        q.append((nx, ny, cs + 1))
                else:
                    break
    dq = deque()
    v = {startX, startY}
    dq.append((startX, startY, 0))
    while dq:
        cl = dq.popleft()
        if cl[:2] == (goalX, goalY):
            return cl[2]
        else:
            next(g, cl, dq, v)


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    first_multiple_input = input().rstrip().split()
    startX = int(first_multiple_input[0])
    startY = int(first_multiple_input[1])
    goalX = int(first_multiple_input[2])
    goalY = int(first_multiple_input[3])
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    fptr.write(str(result) + '\n')
    fptr.close()
