# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Linked Lists: Detect a Cycle
# Sub-Domain : Interview Preparation kit | Linked Lists
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

def has_cycle(head):
    if head is None:
        return False
    s = head
    f = head.next
    while s != f:
        if f is None or f.next is None:
            return False
        s = s.next
        f = f.next.next
    return True
