"""
A Python implementation of the Node class defined in Chapter 2,
with an additional class method for defining linked lists from a normal list.

Author: Christopher Parks
"""


class Node:
    def __init__(self, next: 'Node'=None, data=None):
        self.next = next
        self.data = data

    @classmethod
    def fromList(cls, list:list):
        """
        Creates a linked list of nodes from a list containing the data for each node.
        :param list: List containing the data that will be held in each node.
        :return: A node that represents a linked list.
        """
        data_list = list.copy()
        try:
            head = Node(data=data_list.pop(0))
        except IndexError:  # Blank list.
            return Node()  # Return blank node if list blank.

        for data in data_list:
            head.appendToTail(data)

        return head

    @staticmethod
    def toList(head:'Node'):
        """
        Creates a normal Python list from a Linked List. Good for unit testing.
        :return: List of data values, in the order they appeared from the head.
        """
        return_list = [head.data]
        while head.next is not None:
            return_list.append(head.next.data)
            head = head.next

        return return_list

    def appendToTail(self, data):
        end = Node(data=data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    @staticmethod
    def deleteNode(head: 'Node', data):
        n = head

        if n.data == data:
            return head.next

        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next
                return head
            n = n.next

        return head
