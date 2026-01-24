import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(common_in_nested_lists([]), [])

    def test_single_list(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3]]), [1, 2, 3])

    def test_single_element_lists(self):
        self.assertListEqual(common_in_nested_lists([[1], [2], [3]]), [1, 2, 3])

    def test_overlapping_elements(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [2, 3, 4])

    def test_no_overlapping_elements(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [])

    def test_nested_lists(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, [3, 4]], [2, 3, 4], [3, 4, 5]]), [2, 3, 4])
