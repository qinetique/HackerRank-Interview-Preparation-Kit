# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Insert a node at a specific position in a linked list
# Sub-Domain : Interview Preparation kit | Linked Lists
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtPosition(llist, data, position):
    back = llist
    while position > 1:
        back = back.next
        position -= 1
    node = SinglyLinkedListNode(data)
    node.next = back.next
    back.next = node
    return llist


if __name__ == '__main__':
    fptr = sys.stdout
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    data = int(input())
    position = int(input())
    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')
    fptr.close()
