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
    def kth_to_last(head: Node, k):
        """
        Question 2.2
        Implement an algorithm to find the kth to last element of a singly linked list.
        :param k: Number of elements behind the last which you wish to find. Must be greater than 0.
        :return: The kth node.
        """
        main_cursor = head
        kth_element = None
        i = 1
        while main_cursor.next is not None:  # Loop through to the end
            if i >= k:  # An element we've passed by is possibly the kth element.
                if kth_element is None:  # The first element is possibly the kth element.
                    kth_element = head
                else:  # The next element is possibly the kth element.
                    if kth_element.next is not None:
                        kth_element = kth_element.next
            main_cursor = main_cursor.next
            i += 1

        return kth_element

    @staticmethod
    def delete_middle(head: Node):
        """
        Question 2.3
        Implement an algorithm to delete a node in the middle (i.e., any node but
        the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
        that node.
        :param head: Node that references the head of a linked list
        :return: Linked list with the middle node removed.
        """
        cursor = head  # Cursor used to loop through the entire linked list to count the number of nodes
        middle_cursor = head  # This cursor actually stays one position behind the middle node so its next reference can be updated
        i = 1
        while cursor.next is not None:
            if i > 2 and i % 2 == 0:  # Move middle_cursor forward one
                middle_cursor = middle_cursor.next

            i += 1
            cursor = cursor.next
        middle_cursor.next = middle_cursor.next.next
        return head


    @staticmethod
    def partition(head: Node, value: int):
        """
        Question 2.4
        Write code to partition a linked list around a value x, such that all nodes less than x come
        before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
        to be after the elements less than x (see below). The partition element x can appear anywhere in the
        "right partition"; it does not need to appear between the left and right partitions.
        :param head:
        :return:
        """

    @staticmethod
    def sum_lists(list_1: Node, list_2: Node):
        """
        Question 2.5
        You have two numbers represented by a linked list, where each node contains a single
        digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
        function that adds the two numbers and returns the sum as a linked list.
        :param list_1: Head element of the first linked list.
        :param list_2: Head element of the second linked list.
        :return: Sum of the two lists, in the same format the two lists are given in.
        """