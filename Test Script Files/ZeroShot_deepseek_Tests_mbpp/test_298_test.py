import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(intersection_nested_lists([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(intersection_nested_lists([1], [1]), [[1]])
        self.assertEqual(intersection_nested_lists([1], [2]), [[]])

    def test_multiple_element_lists(self):
        self.assertEqual(intersection_nested_lists([1, 2, 3], [1, 2, 3]), [[1, 2, 3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [3, 2, 1]), [[1, 2, 3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [4, 5, 6]), [[]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [1, 2]), [[1, 2]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [2, 3]), [[2, 3]])

    def test_nested_lists(self):
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3]]), [[1, 2, 3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[3, 2, 1]]), [[1, 2, 3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[4, 5, 6]]), [[]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2]]), [[1, 2]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[2, 3]]), [[2, 3]])
