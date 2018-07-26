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
    def partition(head: Node, partition_val: int):
        """
        Question 2.4
        Write code to partition a linked list around a value x, such that all nodes less than x come
        before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
        to be after the elements less than x (see below). The partition element x can appear anywhere in the
        "right partition"; it does not need to appear between the left and right partitions.
        :param head: Head of the linked list to be partitioned
        :return: Head of a new linked list that is partitioned.
        """
        # Basic idea: Make two linked lists: result, and right
        # Scroll through "head", and append each node that is "left" of x to the "result" list.
        # If it is not to the "left" of x, append it to "right".
        # At the end, set the "next" of the last element of "result" as the head of the "right" linked list.

        result = None  # Will be used to store the head of the result list
        left_cursor = None  # Used to keep track of the last element in the 'left' part of the partition.

        right = None  # Used to store the head of the 'right' part of the partition.
        right_cursor = None  # Used to keep track of the last element in the 'right' part of the partition.

        while head is not None:
            if head.data < partition_val:  # Append to 'left'
                if result:
                    left_cursor.appendToTail(head.data)
                    left_cursor = left_cursor.next
                else:
                    result = Node(data=head.data)
                    left_cursor = result
            else:  # Append to 'right'
                if right:
                    right_cursor.appendToTail(head.data)
                    right_cursor = right_cursor.next
                else:
                    right = Node(data=head.data)
                    right_cursor = right

            head = head.next

        if result and right:
            left_cursor.appendToTail(right)
            return result
        elif result:  # There were no elements greater than or equal to the partition value
            return result
        elif right:  # There were no elements less than the partition value
            return right
        else:  # There were no elements
            return Node()  # Return a blank node

    @staticmethod
    def sum_lists(list_1: Node, list_2: Node):
        """
        Question 2.5
        You have two numbers represented by a linked list, where each node contains a single
        digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
        function that adds the two numbers and returns the sum as a linked list.
        Example input: 617 + 295 ==(7 -> 1 -> 6) + (5 -> 9 -> 2)
        Example output: (2 -> 1 -> 9) == 912
        :param list_1: Head element of the first linked list.
        :param list_2: Head element of the second linked list.
        :return: Sum of the two lists, in the same format the two lists are given in.
        """
        cursor_1 = list_1  # Save and use reference to list_1 to avoid changing list_1's position
        cursor_2 = list_2  # Save and use reference to list_2 to avoid changing list_2's position

        result = Node(data=0)  # Head of the result node
        result_cursor = result  # Save and use reference to head to avoid changing result's head pos

        carry = 0
        while cursor_1 is not None or cursor_2 is not None or carry:  # Runs for O(N) loops, where N is the length of the largest list.
            result_cursor.data += carry  # Process the carried value
            carry = 0  # Reset carry

            if cursor_1:  # Process the data from list 1
                result_cursor.data += cursor_1.data
                cursor_1 = cursor_1.next

            if cursor_2:  # Process the data from list 2
                result_cursor.data += cursor_2.data
                cursor_2 = cursor_2.next

            if result_cursor.data > 9:  # If value 10 or greater, set carry
                carry = 1  # Carry will only ever be a maximum of 1, as 9+9+1 (carry) = 19
                result_cursor.data -= 10

            if cursor_1 or cursor_2 or carry:  # If any of these are true, we must append a node to process what's left
                result_cursor.appendToTail(0)  # Start it at 0, the next loop will add everything up.
                result_cursor = result_cursor.next  # Move the cursor to the node we just appended.

        return result

    @staticmethod
    def is_palindrome(head: Node):
        """
        Question 2.6
        Implement a function to check if a linked list is a palindrome.
        :param head: Head element of the linked list.
        :return: TRUE if it is a palindrome, false otherwise
        """
        # Thoughts: Since the author's linked list (node list?) implementation does not include a "previous" field,
        # I will assume that we should not implement this into our node class.

        # The linked list can be separated into two partitions, pivoting around the midpoint.
        # These two partitions will be exactly the same, if reversed.
        # 1 2 3 4 3 2 1
        #       ^
        # 1 2 3 | 3 2 1

        # 1 2 3 4 4 3 2 1
        #       ^ ^
        # 1 2 3 4 | 4 3 2 1

        # On determination of the midpoint, you can determine the first node of the right partition and
        # the length of the left partition.

        # Determination of the midpoint can be done by shifting the
        # midpoint right by 1 node for every 2 nodes encountered.

        head_cursor = head  # Save reference to head to avoid changing position of the parameter passed
        left_partition_len = 0  # How long the left partition is
        right_part_head = None  # Head of the right partition.
        while head_cursor.next is not None:  # Search for the midpoint
            # Add midpoint search
            # Add left partition length determinator
            head_cursor = head_cursor.next  # Advance to the next node

        # Set right_partition_head

    @staticmethod
    def is_intersection(list_1: Node, list_2: Node):
        """
        Question 2.7
        Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
        Note that the intersection is defined based on reference, not value.
        That is, if the kth node of the first linked list is the exact same node (by reference) as
            the jth node of the second linked list, then they are intersecting.
        :param list_1: First singly linked list
        :param list_2: Second singly linked list
        :return: The intersecting node, if they intersect. Blank node if they do not.
        """
        # The O(N^2) method is obvious: while list_1, while list_2, if node == node return True
        # But how can we do it in O(N)?

        # Both lists will have at least 1 node in common if they intersect.
        # Past the point of intersection, they should both be the same.
        # Ex: A->B->C->D->E
        #     H->I->J->C->D->E

    @staticmethod
    def loop_detection(head: Node):
        """
        Question 2.8
        Given a circular linked list, implement an algorithm that returns the node at the
        beginning of the loop.

        DEFINITION
        Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
        as to make a loop in the linked list.

        EXAMPLE
        Input: A -> B -> C -> D -> E -> C [the same C as earlier]
        Output: C
        :param head:
        :return:
        """