from unittest import TestCase
from linked_list_questions import LinkedListQuestions
from LinkedList import Node


class TestLinkedListQuestions(TestCase):
    def test_remove_duplicates(self):
        test_cases = [([1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
                      ([1, 2, 3, 4, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
                      ([1, 1, 2, 1, 3, 4, 4, 3, 2, 5, 3, 3, 5, 6, 6, 6], [1, 2, 3, 4, 5, 6]),
                      ([1, 1, 1, 1], [1]),
                      ([], [None])]

        for test_list, result in test_cases:
            self.assertListEqual(Node.toList(LinkedListQuestions.remove_duplicates(Node.fromList(test_list))), result)

    def test_kth_to_last(self):
        pass#self.fail()
