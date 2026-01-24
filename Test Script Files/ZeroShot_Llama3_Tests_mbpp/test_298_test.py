import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_intersection_nested_lists(self):
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [1, 2, 3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [[4, 5, 6], [7, 8, 9]]), [[], [], []])
        self.assertEqual(intersection_nested_lists([1, 2, 3], []), [])
        self.assertEqual(intersection_nested_lists([], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[], [], []])
        self.assertEqual(intersection_nested_lists([], []), [])

    def test_intersection_nested_lists_empty_list(self):
        self.assertEqual(intersection_nested_lists([], []), [])

    def test_intersection_nested_lists_single_element(self):
        self.assertEqual(intersection_nested_lists([1], [[1], [2, 3]]), [[1], [1]])
        self.assertEqual(intersection_nested_lists([1], [[2, 3]]), [[], []])
