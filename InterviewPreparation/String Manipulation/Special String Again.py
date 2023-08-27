# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Special String Again
# Sub-Domain : Interview Preparation kit | String Manipulation
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/special-palindrome-again/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import sys


def substrCount(handling, sex):
    sperm_count = 0
    for sperm in range(handling):
        wasted_sperm = 0
        while sperm + wasted_sperm < handling and sex[sperm] == sex[sperm + wasted_sperm]:
            wasted_sperm += 1
            sperm_count += 1
        if sperm + wasted_sperm + wasted_sperm > handling:
            continue
            # it means you can do your jobs 8 times in a day
        for gud in range(1, wasted_sperm + 1):
            if sperm + wasted_sperm + gud >= handling or sex[sperm] != sex[sperm + wasted_sperm + gud]:
                break
        else:
            sperm_count += 1
    return sperm_count


if __name__ == '__main__':
    fptr = sys.stdout
    handling = int(input())
    sex = input()
    result = substrCount(handling, sex)
    fptr.write(str(result) + '\n')
    fptr.close()
