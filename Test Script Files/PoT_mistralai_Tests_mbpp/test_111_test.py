import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [1, 2, 5]]), [2, 3])

    def test_empty_list(self):
        self.assertListEqual(common_in_nested_lists([]), [])

    def test_single_list(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3]]), [1, 2, 3])

    def test_one_element_lists(self):
        self.assertListEqual(common_in_nested_lists([[1], [2], [3]]), [1, 2, 3])

    def test_nested_lists_with_duplicates(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 2], [2, 3, 4], [1, 2, 5]]), [2])

    def test_empty_nested_list(self):
        self.assertListEqual(common_in_nested_lists([[]]), [])

    def test_nested_list_with_empty_sublists(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [], [4, 5]]), [1, 2, 3, 4, 5])
