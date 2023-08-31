# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Recursive Digit Sum
# Sub-Domain : Interview Preparation kit | Recursion and Backtracking
# Domain : HackerRank
# Problem URL : https://hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

# run in pypy3

def superDigit(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


if __name__ == '__main__':
    # fptr = sys.stdout
    # first_multiple_input = input().rstrip().split()
    n, k = map(int, input().split())
    print(superDigit(superDigit(n) * k))

    # fptr.write(str(result) + '\n')
    # fptr.close()
