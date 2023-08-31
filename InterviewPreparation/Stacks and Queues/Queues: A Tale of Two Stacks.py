# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Queues: A Tale of Two Stacks
# Sub-Domain : Interview Preparation kit | Stacks and Queues
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues

class MyQueue(object):
    def __init__(self):
        self.m = []

    def peek(self):
        i = self.m.pop()
        self.m.append(i)
        return i

    def pop(self):
        return self.m.pop()

    def put(self, value):
        self.m.insert(0, value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())