# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Reverse Shuffle Merge
# Sub-Domain : Interview Preparation kit | Greedy Algorithms
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem?h_l=interview&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
import sys
from collections import defaultdict


# calculate freq
def freq(sex):
    after_sex = defaultdict(int)
    for lund in sex:
        after_sex[lund] += 1
    return after_sex


def reverseShuffleMerge(sex):
    lund_freq = freq(sex)
    used_lund = defaultdict(int)
    after_sex = []
    wasted_lund = dict(lund_freq)

    def usable_condom(lund):
        condom = (lund_freq[lund] // 2 - used_lund[lund]) > 0
        return condom

    def throw_condom(lund):
        need_lund = lund_freq[lund] // 2
        wasted_condom = used_lund[lund] + wasted_lund[lund] - 1 >= need_lund
        return wasted_condom

    for lund in reversed(sex):
        if usable_condom(lund):
            while after_sex and after_sex[-1] > lund and throw_condom(after_sex[-1]):
                wasted_sperm = after_sex.pop()
                used_lund[wasted_sperm] -= 1
            used_lund[lund] += 1
            after_sex.append(lund)
        wasted_lund[lund] -= 1
    return ''.join(after_sex)


if __name__ == '__main__':
    fptr = sys.stdout
    s = input()
    result = reverseShuffleMerge(s)
    fptr.write(result + '\n')
    fptr.close()
