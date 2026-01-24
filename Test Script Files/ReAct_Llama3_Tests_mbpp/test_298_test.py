import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(intersection_nested_lists([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(intersection_nested_lists([1], [1, 2, 3]), [[1]])
        self.assertEqual(intersection_nested_lists([1, 2, 3], [1]), [[1]])

    def test_multiple_elements_lists(self):
        self.assertEqual(intersection_nested_lists([1, 2, 3], [1, 2, 3, 4, 5]), [[1], [2], [3]])
        self.assertEqual(intersection_nested_lists([1, 2, 3, 4, 5], [1, 2, 3]), [[1], [2], [3]])

    def test_non_intersecting_lists(self):
        self.assertEqual(intersection_nested_lists([1, 2, 3], [4, 5, 6]), [])

    def test_intersecting_lists_with_duplicates(self):
        self.assertEqual(intersection_nested_lists([1, 2, 2, 3], [1, 2, 2, 3, 4, 5]), [[1], [2, 2], [3]])

    def test_intersecting_lists_with_duplicates_and_empty_lists(self):
        self.assertEqual(intersection_nested_lists([1, 2, 2, 3], []), [])
        self.assertEqual(intersection_nested_lists([], [1, 2, 2, 3]), [])
