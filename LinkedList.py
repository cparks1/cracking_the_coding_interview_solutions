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
        try:
            head = Node(data=list.pop(0))
        except IndexError:  # Blank list.
            return Node()  # Return blank node if list blank.

        for data in list:
            head.appendToTail(data)

        return head

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