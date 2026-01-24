import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_simple_list_of_lists(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [3, 4, 5], [1, 3]]), [1, 3])

    def test_empty_list(self):
        self.assertListEqual(common_in_nested_lists([]), [])

    def test_list_with_single_element(self):
        self.assertListEqual(common_in_nested_lists([[1]]), [1])

    def test_list_with_multiple_elements(self):
        self.assertListEqual(common_in_nested_lists([[1], [2], [3]]), [])

    def test_list_with_duplicates(self):
        self.assertListEqual(common_in_nested_lists([[1, 1], [2, 2], [3, 3]]), [1, 2, 3])

    def test_list_with_nested_lists(self):
        self.assertListEqual(common_in_nested_lists([[1, [2]], [3, [2]], [1, [3]]]), [1, 2, 3])

    def test_list_with_empty_nested_lists(self):
        self.assertListEqual(common_in_nested_lists([[1, []], [2, []], [3, []]]), [1, 2, 3])

    def test_list_with_mixed_types(self):
        self.assertListEqual(common_in_nested_lists([[1, 2], [3, 'a'], [1, 3]]), [1, 3])
