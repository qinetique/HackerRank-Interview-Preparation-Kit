# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : New Year Chaos
# Sub-Domain : Interview Preparation kit | Arrays
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def minimumBribes(q):
    v = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                v += 1
    print(v)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
