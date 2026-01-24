import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_simple_case(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2], [2, 3], [3]])

    def test_empty_lists(self):
        l1 = []
        l2 = [[]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[]])

    def test_no_intersection(self):
        l1 = [1, 2, 3]
        l2 = [[4, 5], [6, 7], [8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[], [], []])

    def test_single_element(self):
        l1 = [1]
        l2 = [[1], [2], [3]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1], [1], [1]])

    def test_all_elements_in_nested_lists(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    def test_duplicates_in_nested_lists(self):
        l1 = [1, 2, 2]
        l2 = [[1, 2, 2], [2, 2, 1], [2, 1, 2]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 2], [1, 2, 2], [1, 2, 2]])
