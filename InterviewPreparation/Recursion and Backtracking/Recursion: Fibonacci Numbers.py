# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Recursion: Fibonacci Numbers
# Sub-Domain : Interview Preparation kit | Recursion and Backtracking
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

def fibonacci(num):
    if num == 0:
        return  0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


n = int(input())
print(fibonacci(n))
