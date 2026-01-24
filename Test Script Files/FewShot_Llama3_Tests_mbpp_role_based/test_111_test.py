import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):
    def test_common_elements(self):
        nested_list = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        self.assertEqual(common_in_nested_lists(nested_list), [3])

    def test_empty_list(self):
        nested_list = []
        self.assertEqual(common_in_nested_lists(nested_list), [])

    def test_single_element_list(self):
        nested_list = [[1]]
        self.assertEqual(common_in_nested_lists(nested_list), [1])

    def test_no_common_elements(self):
        nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(common_in_nested_lists(nested_list), [])

    def test_common_elements_in_sublists(self):
        nested_list = [[1, 2, 3], [2, 3, 4], [3, 4, 5, 6]]
        self.assertEqual(common_in_nested_lists(nested_list), [3, 4])
