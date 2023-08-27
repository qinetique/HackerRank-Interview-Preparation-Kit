# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Hash Tables: Ice Cream Parlor
# Sub-Domain : Interview Preparation kit | Search
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

def whatFlavors(cost, money):
    var = {}
    for x, y in enumerate(cost):
        if money - y in var.keys():
            print('{} {}'.format(var[money - y] + 1, x + 1))
        var[y] = x
    return


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
