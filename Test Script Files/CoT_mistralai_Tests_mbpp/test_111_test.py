import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], common_in_nested_lists([]))

    def test_single_list(self):
        self.assertListEqual([1], common_in_nested_lists([[1], [1]]))
        self.assertListEqual([], common_in_nested_lists([[1], [2]]))

    def test_multiple_lists_same_elements(self):
        self.assertListEqual([1, 2], common_in_nested_lists([[1, 2], [2, 1], [1, 3, 2]]))

    def test_multiple_lists_different_elements(self):
        self.assertListEqual([], common_in_nested_lists([[1, 2], [3, 4], [1, 3]]))

    def test_nested_lists(self):
        self.assertListEqual([1], common_in_nested_lists([[1], [[1]]]))
        self.assertListEqual([], common_in_nested_lists([[1], [[2]]]))
        self.assertListEqual([1, 2], common_in_nested_lists([[1, 2], [[1, 2]], [[1], [2]]]))

    def test_invalid_input(self):
        self.assertRaises(TypeError, common_in_nested_lists, 123)
