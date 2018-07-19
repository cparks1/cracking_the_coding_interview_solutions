from unittest import TestCase
from linked_list_questions import LinkedListQuestions
from LinkedList import Node

class TestLinkedListQuestions(TestCase):
    def test_remove_duplicates(self):
        test_list = [1,2,3,4,4,4,5,5,6]
        list_no_dups = Node.toList(LinkedListQuestions.remove_duplicates(Node.fromList(test_list)))

        print(list_no_dups)

        pass#self.fail()

    def test_kth_to_last(self):
        pass#self.fail()
