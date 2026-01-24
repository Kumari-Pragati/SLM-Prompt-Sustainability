import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], common_in_nested_lists([]))

    def test_single_list(self):
        self.assertListEqual([1], common_in_nested_lists([[1]]))
        self.assertListEqual([2], common_in_nested_lists([[2]]))

    def test_two_lists_with_common_elements(self):
        self.assertListEqual([1, 2], common_in_nested_lists([[1, 2], [2, 1]]))

    def test_two_lists_with_no_common_elements(self):
        self.assertListEqual([], common_in_nested_lists([[1, 2], [3, 4]]))

    def test_list_of_lists_with_common_elements(self):
        self.assertListEqual([1, 2], common_in_nested_lists([[1, 2], [2, 1], [3, 1]]))

    def test_list_of_lists_with_no_common_elements(self):
        self.assertListEqual([], common_in_nested_lists([[1, 2], [3, 4], [5, 6]]))

    def test_list_of_lists_with_empty_sublists(self):
        self.assertListEqual([], common_in_nested_lists([[1, 2], [], [3, 4]]))

    def test_list_of_lists_with_mixed_types(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists([[1, 2], [3, '4'], [5, 6]])
