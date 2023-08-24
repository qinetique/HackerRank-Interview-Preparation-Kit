# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Counting Valleys
# Sub-Domain : Interview Preparation kit | Warm-up Challenges
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def solution(steps, path):
    lv = 0
    v = 0
    inside_v = False

    for i in path:
        if i == 'U':
            lv += 1
        else:
            lv -= 1
        if lv < 0:
            inside_v = True
        elif lv == 0 and inside_v:
            v += 1
            inside_v = False
    return v


steps = int(input())
path = input().strip()

sol = solution(steps, path)
print(sol)
