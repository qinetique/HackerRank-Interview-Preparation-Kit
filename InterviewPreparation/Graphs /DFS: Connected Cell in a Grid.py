# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : DFS: Connected Cell in a Grid
# Sub-Domain : Interview Preparation kit | Graphs
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/matrix/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import sys


def maxRegion(grid):
    m_region = 0
    r_s = len(grid)
    c_s = len(grid[0])
    v = [[False for _ in range(c_s)] for _ in range(r_s)]
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if grid[i][j] == 1:
                rs = c_region(grid, i, j, v)
                m_region = max(m_region, rs)
    return m_region


def c_region(grid, r, c, v):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return 0
    if v[r][c] is True:
        return 0
    v[r][c] = True
    if grid[r][c] == 0:
        return 0
    s = 1
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i != r or j != c:
                s += c_region(grid, i, j, v)
    return s


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))
    res = maxRegion(grid)
    fptr.write(str(res) + '\n')
    fptr.close()
