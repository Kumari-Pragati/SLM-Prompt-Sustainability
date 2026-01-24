import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(common_in_nested_lists([]), [])

    def test_single_element_list(self):
        self.assertEqual(common_in_nested_lists([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(common_in_nested_lists([1, 2, 3]), [1, 2, 3])

    def test_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])

    def test_empty_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[], [], []]), [])

    def test_common_elements_in_sublists(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])

    def test_no_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [])

    def test_common_elements_in_sublists_with_duplicates(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2, 3], [2, 3, 3, 4], [3, 4, 4, 5]]), [3])
