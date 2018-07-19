from LinkedList import Node
from collections import defaultdict


class LinkedListQuestions:
    @staticmethod
    def remove_duplicates(linked_list:Node):
        """
        Question 2.1
        Write code to remove duplicates from an unsorted linked list.
        :return: Unsorted linked list with duplicates removed.
        """
        val_count = defaultdict(int)  # Dictionary to keep track of the count of how many times a value has appeared.

        while linked_list.next is not None:
            val_count[linked_list.data] += 1

            while val_count[linked_list.next.data] > 1:  # Begin searching for an element that is not a duplicate
                val_count[linked_list.next.data] += 1
                linked_list.next = linked_list.next.next

            linked_list = linked_list.next  # Move to the next position

        return linked_list

    @staticmethod
    def kth_to_last():
        """
        Question 2.2
        Implement an algorithm to find the kth to last element of a singly linked list.
        :return:
        """