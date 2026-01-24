import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(intersection_nested_lists([[1, 2, 3], [4, 2, 1, 3]],
                                                        [[1, 2, 3], [4, 5], [1, 2, 3]]),
                              [[1, 2, 3]])

    def test_empty_lists(self):
        self.assertListEqual(intersection_nested_lists([], []), [])

    def test_one_empty_list(self):
        self.assertListEqual(intersection_nested_lists([[1, 2, 3]], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(intersection_nested_lists([[1]], [[1]]), [[1]])
        self.assertListEqual(intersection_nested_lists([[1]], [[2]]), [])

    def test_nested_lists_with_different_lengths(self):
        self.assertListEqual(intersection_nested_lists([[1, 2], [3]], [[1, 2, 3], [4]]), [])

    def test_nested_lists_with_no_intersection(self):
        self.assertListEqual(intersection_nested_lists([[1, 2], [3]], [[4, 5], [6]]), [])

    def test_nested_lists_with_duplicates(self):
        self.assertListEqual(intersection_nested_lists([[1, 2], [3]], [[1, 2, 1], [3]]), [[1, 2]])
