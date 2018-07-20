from LinkedList import Node
from collections import defaultdict


class LinkedListQuestions:
    @staticmethod
    def remove_duplicates(head:Node):
        """
        Question 2.1
        Write code to remove duplicates from an unsorted linked list.
        :return: Unsorted linked list with duplicates removed.
        """
        val_count = defaultdict(int)  # Dictionary to keep track of the count of how many times a value has appeared.

        head_ref_save = head  # Save the head position so we may return it after operating

        while head is not None and head.next is not None:
            val_count[head.data] += 1

            while head.next is not None and val_count[head.next.data] >= 1:  # Begin searching for an element that is not a duplicate
                val_count[head.next.data] += 1
                head.next = head.next.next

            head = head.next  # Move to the next position

        return head_ref_save

    @staticmethod
    def kth_to_last():
        """
        Question 2.2
        Implement an algorithm to find the kth to last element of a singly linked list.
        :return:
        """