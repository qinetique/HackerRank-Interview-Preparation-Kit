# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Common Child
# Sub-Domain : Interview Preparation kit | String Manipulation
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
import sys


#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(sexx, sexy):
    last_sex = [0] * (len(sexx) + 1)
    for sperm in range(1, len(sexx) + 1):
        no_sex = [0]
        for wasted_sperm in range(1, len(sexy) + 1):
            if sexx[sperm - 1] == sexy[wasted_sperm - 1]:
                no_sex.append(last_sex[wasted_sperm - 1] + 1)
            else:
                no_sex.append(max(last_sex[wasted_sperm], no_sex[-1]))
        last_sex = no_sex
    return last_sex[-1]


if __name__ == '__main__':
    fptr = sys.stdout
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()
