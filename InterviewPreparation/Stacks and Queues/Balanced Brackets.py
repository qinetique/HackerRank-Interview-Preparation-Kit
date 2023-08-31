# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Balanced Brackets
# Sub-Domain : Interview Preparation kit | Stacks and Queues
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
import sys


def isBalanced(s):
    v = []
    my_seq = {'(': ')', '[': ']', '{': '}'}
    for i in s:
        if i in my_seq.keys():
            v.append(i)
        elif len(v) == 0 or my_seq[v.pop()] != i:
            return 'NO'
    if len(v) > 0:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = sys.stdout
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
