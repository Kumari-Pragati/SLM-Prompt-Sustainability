import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):
    def test_typical_use_case(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [], []])

    def test_empty_lists(self):
        l1 = []
        l2 = [[]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[]])

    def test_one_empty_list(self):
        l1 = [1, 2, 3]
        l2 = [[]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[]])

    def test_no_common_elements(self):
        l1 = [1, 2, 3]
        l2 = [[4, 5, 6], [7, 8, 9]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[], []])

    def test_all_common_elements(self):
        l1 = [1, 2, 3]
        l2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    def test_duplicate_common_elements(self):
        l1 = [1, 2, 2]
        l2 = [[1, 2, 2], [1, 2, 2], [1, 2, 2]]
        self.assertEqual(intersection_nested_lists(l1, l2), [[1, 2, 2], [1, 2, 2], [1, 2, 2]])
