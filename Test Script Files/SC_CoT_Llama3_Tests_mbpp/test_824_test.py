import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(remove_even([2]), [])

    def test_edge_case_list_with_single_even_element(self):
        self.assertEqual(remove_even([1, 2, 3]), [1, 3])

    def test_edge_case_list_with_multiple_even_elements(self):
        self.assertEqual(remove_even([2, 4, 6, 8]), [])

    def test_edge_case_list_with_single_odd_element(self):
        self.assertEqual(remove_even([1, 2, 3, 5]), [1, 3, 5])

    def test_edge_case_list_with_multiple_odd_elements(self):
        self.assertEqual(remove_even([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_edge_case_list_with_mixed_elements(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            remove_even("test")

    def test_invalid_input_non_integer_list(self):
        with self.assertRaises(TypeError):
            remove_even(["a", "b", "c"])
