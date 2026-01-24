import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(common_in_nested_lists([]), [])

    def test_single_element_list(self):
        self.assertEqual(common_in_nested_lists([[1]]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(common_in_nested_lists([[1, 2], [2, 3]]), [2])

    def test_common_elements_in_multiple_lists(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])

    def test_common_elements_in_multiple_lists_with_duplicates(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2, 3], [2, 2, 3, 4], [3, 4, 5, 5]]), [2, 3])

    def test_common_elements_in_multiple_lists_with_duplicates_and_empty_lists(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2, 3], [2, 2, 3, 4], [], [3, 4, 5, 5]]), [2, 3])

    def test_common_elements_in_multiple_lists_with_duplicates_and_empty_lists_and_single_element_list(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2, 3], [2, 2, 3, 4], [], [3, 4, 5, 5], [5]]), [2, 3, 5])
