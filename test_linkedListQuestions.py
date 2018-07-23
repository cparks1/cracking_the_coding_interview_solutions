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
            self.assertListEqual(result, Node.toList(LinkedListQuestions.remove_duplicates(Node.fromList(test_list))))

    def test_kth_to_last(self):
        test_cases = [([1, 2, 3, 4], 1),
                      ([1, 5, 3, 2, 4, 8, 23], 3),
                      ([1, 67, 38, 83, 23, 54, 63], 3),
                      ([17, 67, 83, 38, 32, 45, 36], 7)]

        for test_list, k in test_cases:
            testNode = Node.fromList(test_list)
            if k < len(test_list):
                self.assertEqual(test_list[(k*-1)-1], LinkedListQuestions.kth_to_last(testNode, k).data)
            else:
                self.assertIsNone(LinkedListQuestions.kth_to_last(testNode, k))

    def list_delete_middle(self, list):
        middle = int(len(list)/2)
        list.pop(middle if len(list) % 2 != 0 else middle-1)

    def test_delete_middle(self):
        testNodes = [[1, 2, 3, 4, 5],
                     [1, 2, 3, 4],
                     [1, 2, 3, 4, 5, 6, 7]]
        for nodeList in testNodes:
            testNode = Node.fromList(nodeList)
            self.list_delete_middle(nodeList)
            LinkedListQuestions.delete_middle(testNode)

            self.assertListEqual(nodeList, Node.toList(testNode))

    def test_sum_lists(self):
        test_cases = [([3, 2, 1], [1, 2, 3], [4, 4, 4]),
                      ([7, 1, 6], [5, 9, 2], [2, 1, 9])]
        for nodeList1, nodeList2, resultList in test_cases:
            list1 = Node.fromList(nodeList1)
            list2 = Node.fromList(nodeList2)
            resultNodeList = LinkedListQuestions.sum_lists(list1, list2)
            self.assertListEqual(resultList, Node.toList(resultNodeList))
