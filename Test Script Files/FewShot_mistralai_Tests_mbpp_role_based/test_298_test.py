import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(intersection_nested_lists([], []), [])

    def test_single_list(self):
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1], [2, 3], [4]]), [[1]])

    def test_nested_lists(self):
        self.assertListEqual(intersection_nested_lists([1, [2, 3], [4]], [[1], [2, 3], [4]]), [[1], [2, 3]])

    def test_empty_elements(self):
        self.assertListEqual(intersection_nested_lists([[], [1, 2], [3]], [[1], [], [3]]), [[3]])

    def test_non_matching_elements(self):
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[4], [5], [6]]), [])
