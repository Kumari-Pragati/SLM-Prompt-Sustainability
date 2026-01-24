import unittest
from mbpp_298_code import intersection_nested_lists

class TestIntersectionNestedLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual([], intersection_nested_lists([], []))

    def test_single_level_lists(self):
        self.assertListEqual([1, 2, 3], intersection_nested_lists([1, 2, 3], [4, 1, 2, 3, 5]))
        self.assertListEqual([], intersection_nested_lists([6, 7, 8], [4, 1, 2, 3, 5]))

    def test_multi_level_lists(self):
        self.assertListEqual([1, 2], intersection_nested_lists([[1, 2], [3, 2]], [[1, 2], [3, 2], [4, 1]]))
        self.assertListEqual([], intersection_nested_lists([[6, 7], [8, 9]], [[4, 1], [2, 3]]))

    def test_nested_lists_with_duplicates(self):
        self.assertListEqual([1, 2], intersection_nested_lists([[1, 2], [1, 2]], [[1, 2], [3, 2], [1, 2]]))

    def test_empty_input_list(self):
        with self.assertRaises(TypeError):
            intersection_nested_lists([], [1, 2, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            intersection_nested_lists('str', [1, 2, 3])
