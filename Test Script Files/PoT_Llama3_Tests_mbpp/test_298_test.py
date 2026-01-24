import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):
    def test_typical_case(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [], []])

    def test_edge_case_empty_list1(self):
        l1 = []
        l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[], [], []])

    def test_edge_case_empty_list2(self):
        l1 = [1, 2, 3]
        l2 = []
        self.assertEqual(intersection_nested_lists(l1, l2), [])

    def test_edge_case_single_element_list1(self):
        l1 = [1]
        l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1], [], []])

    def test_edge_case_single_element_list2(self):
        l1 = [1, 2, 3]
        l2 = [[1], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1], [], []])

    def test_edge_case_single_element_list3(self):
        l1 = [1]
        l2 = [[1, 2, 3], [1, 4, 5], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1], [1], []])

    def test_edge_case_single_element_list4(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [1, 4, 5], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [1, 4, 5], []])

    def test_edge_case_empty_list1_and_empty_list2(self):
        l1 = []
        l2 = []
        self.assertEqual(intersection_nested_lists(l1, l2), [])
