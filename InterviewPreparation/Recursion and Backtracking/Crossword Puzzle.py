# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Crossword Puzzle
# Sub-Domain : Interview Preparation kit | Recursion and Backtracking
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

n = 10


def crosswordPuzzle():
    crossword = [list(input()) for _ in range(n)]
    words = input().split(';')
    pos = set()
    for i in range(n):
        for j in range(n):
            if crossword[i][j] == '-':
                if (i == 0 or crossword[i - 1][j] != '-') and (i == n - 1 or crossword[i + 1][j] == '-'):
                    pos.add((i, j, 1, 0))
                if (j == 0 or crossword[i][j - 1] != '-') and (j == n - 1 or crossword[i][j + 1] == '-'):
                    pos.add((i, j, 0, 1))
    solution(crossword, words, pos)


def solution(crosswords, words, pos):
    if not words:
        print(fts(crosswords))
        exit()
    words, w = words[:-1], words[-1]
    for p in pos:
        i, j, ii, jj = p
        nxt = True
        nxt_cw = [x[:] for x in crosswords]
        for a in w:
            if i > n - 1 or j > n - 1 or nxt_cw[i][j] != '-' and nxt_cw[i][j] != a:
                nxt = False
                break
            nxt_cw[i][j] = a
            i += ii
            j += jj
        if i < n and j < n and nxt_cw[i][j] == '-':
            nxt = False
        if nxt:
            n_pos = pos.copy()
            n_pos.remove(p)
            solution(nxt_cw, words, n_pos)


def fts(f):
    return '\n'.join(map(''.join, f))


if __name__ == '__main__':
    crosswordPuzzle()
