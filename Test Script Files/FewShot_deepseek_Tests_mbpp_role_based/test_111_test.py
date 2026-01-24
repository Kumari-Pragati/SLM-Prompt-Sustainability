import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])

    def test_empty_nested_list(self):
        self.assertEqual(common_in_nested_lists([[], []]), [])

    def test_single_element_in_nested_list(self):
        self.assertEqual(common_in_nested_lists([[1], [1]]), [1])

    def test_no_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6]]), [])

    def test_empty_nested_list_with_common_elements(self):
        self.assertEqual(common_in_nested_lists([[], [1, 2, 3]]), [])

    def test_single_element_in_nested_list_with_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1], [1, 2, 3]]), [1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists(123)
