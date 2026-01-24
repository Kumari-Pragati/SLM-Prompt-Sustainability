import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1, 2], [3, 4]]), [[1, 2], [3]])
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1], [2, 3], [4]]), [[1], [2, 3]])
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1, 2], [3, 4], [5]]), [])

    def test_edge_cases(self):
        self.assertListEqual(intersection_nested_lists([], []), [])
        self.assertListEqual(intersection_nested_lists([1], []), [])
        self.assertListEqual(intersection_nested_lists([], [[]]), [[]])
        self.assertListEqual(intersection_nested_lists([1], [[1]]), [[1]])

    def test_complex(self):
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1, 2], [2, 3], [3, 4]]), [[2]])
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5], [6, 7]]), [])
        self.assertListEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [1, 2, 4]]), [[1, 2]])
