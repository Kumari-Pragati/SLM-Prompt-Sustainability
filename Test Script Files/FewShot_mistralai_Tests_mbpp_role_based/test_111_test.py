import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(common_in_nested_lists([]), [])
        self.assertListEqual(common_in_nested_lists([[]]), [])
        self.assertListEqual(common_in_nested_lists([[], []]), [])

    def test_single_list(self):
        self.assertListEqual(common_in_nested_lists([1, 2, 3]), [1, 2, 3])

    def test_two_lists(self):
        self.assertListEqual(common_in_nested_lists([1, 2, 3], [3, 4, 5]), [3])
        self.assertListEqual(common_in_nested_lists([1, 2, 3], [2, 4, 5]), [2])

    def test_three_lists(self):
        self.assertListEqual(common_in_nested_lists([1, 2, 3], [3, 4, 5], [6, 7, 3]), [3])

    def test_lists_with_duplicates(self):
        self.assertListEqual(common_in_nested_lists([1, 1, 2, 3], [3, 4, 5]), [1, 3])

    def test_lists_with_nested_lists(self):
        self.assertListEqual(common_in_nested_lists([[1, 2], [3, 4], [1, 3]]), [1, 3])
        self.assertListEqual(common_in_nested_lists([[1, 2], [3, 4], [1, 3]], [[1, 2], [3, 4], [1, 3]]), [1, 3])

    def test_lists_with_empty_elements(self):
        self.assertListEqual(common_in_nested_lists([[], 1, 2]), [])
        self.assertListEqual(common_in_nested_lists([1, [], 2]), [1, 2])
        self.assertListEqual(common_in_nested_lists([[], 1, 2], [1, [], 2]), [1, 2])
