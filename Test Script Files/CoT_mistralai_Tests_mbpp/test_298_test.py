import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual([], intersection_nested_lists([], []))

    def test_single_list_no_intersection(self):
        self.assertListEqual([], intersection_nested_lists([1, 2, 3], [4, 5, 6]))

    def test_single_list_intersection(self):
        self.assertListEqual([2], intersection_nested_lists([1, 2, 2, 3], [1, 2, 3]))

    def test_multiple_lists_intersection(self):
        self.assertListEqual([2, 3], intersection_nested_lists([[1, 2, 2, 3], [4, 2, 3]], []))
        self.assertListEqual([2, 3], intersection_nested_lists([[1, 2, 2, 3], [4, 2, 3]], [[4, 2, 3]]))
        self.assertListEqual([], intersection_nested_lists([[1, 2, 2, 3], [4, 2, 3]], [[4, 5, 6]]))

    def test_nesting_levels(self):
        self.assertListEqual([2], intersection_nested_lists([[1, 2, 2, 3], [4, 2, 3]], [[[4, 2, 3]]]))
        self.assertListEqual([2], intersection_nested_lists([[[1, 2, 2, 3]], [[4, 2, 3]]], []))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            intersection_nested_lists(1, [])

    def test_invalid_input_2(self.assertRaises(TypeError):
        intersection_nested_lists([], 1)
