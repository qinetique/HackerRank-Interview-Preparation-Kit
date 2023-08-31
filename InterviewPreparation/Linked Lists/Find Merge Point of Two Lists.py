# Author : Tonmoy M
# Author URL : https://qinetique.github.io
# Problem : Find Merge Point of Two Lists
# Sub-Domain : Interview Preparation kit | Linked Lists
# Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
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


def findMergeNode(head1, head2):
    v1 = head1
    v2 = head2
    while v1 != v2:
        v1 = v1.next if v1.next is not None else head2
        v2 = v2.next if v2.next is not None else head1
    return v1.data


if __name__ == '__main__':
    fptr = sys.stdout
    tests = int(input())
    for tests_itr in range(tests):
        index = int(input())
        llist1_count = int(input())
        llist1 = SinglyLinkedList()
        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
        llist2_count = int(input())
        llist2 = SinglyLinkedList()
        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
        ptr1 = llist1.head;
        ptr2 = llist2.head;
        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
        for i in range(llist2_count):
            if i != llist2_count - 1:
                ptr2 = ptr2.next
        ptr2.next = ptr1
        result = findMergeNode(llist1.head, llist2.head)
        fptr.write(str(result) + '\n')
    fptr.close()