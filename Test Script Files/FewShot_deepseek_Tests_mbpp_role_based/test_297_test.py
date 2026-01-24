import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(flatten_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(flatten_list([[1]]), [1])

    def test_nested_list_with_single_element(self):
        self.assertEqual(flatten_list([[1, 2], [3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_nested_list_with_empty_sublist(self):
        self.assertEqual(flatten_list([[1, 2, []], [3, 4, 5], [6]]), [1, 2, 3, 4, 5, 6])

    def test_nested_list_with_single_element_sublist(self):
        self.assertEqual(flatten_list([[1, 2, [3]], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_nested_list_with_multiple_levels(self):
        self.assertEqual(flatten_list([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            flatten_list(123)
