# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Reverse a doubly linked list
# Sub-Domain : Interview Preparation kit | Linked Lists
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def reverse(llist):
    solution = llist
    while llist is not None:
        llist.prev, llist.next = llist.next, llist.prev
        solution = llist
        llist = llist.prev
    return solution


if __name__ == '__main__':
    fptr = sys.stdout
    t = int(input())
    for t_itr in range(t):
        llist_count = int(input())
        llist = DoublyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        llist1 = reverse(llist.head)
        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')
    fptr.close()
