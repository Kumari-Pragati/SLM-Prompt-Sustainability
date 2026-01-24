import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):
    def test_common_in_nested_lists_typical(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])

    def test_common_in_nested_lists_empty_list(self):
        self.assertEqual(common_in_nested_lists([]), [])

    def test_common_in_nested_lists_single_element_list(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3]]), [1, 2, 3])

    def test_common_in_nested_lists_multiple_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [2, 3, 4])

    def test_common_in_nested_lists_no_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6]]), [])

    def test_common_in_nested_lists_duplicates(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2], [2, 2, 3]]), [2])

    def test_common_in_nested_lists_empty_sublists(self):
        self.assertEqual(common_in_nested_lists([[], [1, 2, 3]]), [])

    def test_common_in_nested_lists_empty_sublists_multiple(self):
        self.assertEqual(common_in_nested_lists([[], [], [1, 2, 3]]), [])
