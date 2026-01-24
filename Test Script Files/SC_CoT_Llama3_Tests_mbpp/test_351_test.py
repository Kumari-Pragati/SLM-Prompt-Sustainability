import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_case_k_zero(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 0), -1)

    def test_edge_case_k_equal_to_length(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 5), 5)

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 6), -1)

    def test_edge_case_k_equal_to_one(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_case_k_equal_to_length_half(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 3), 3)

    def test_edge_case_k_equal_to_length_third(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 2), 2)

    def test_edge_case_k_equal_to_length_last(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_invalid_input_non_integer_k(self):
        with self.assertRaises(TypeError):
            first_Element([1, 2, 3, 4, 5], 5, 'k')

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            first_Element([1, 2, 3, 4, 5], 'n', 1)

    def test_invalid_input_non_list_arr(self):
        with self.assertRaises(TypeError):
            first_Element('arr', 5, 1)

    def test_invalid_input_empty_list(self):
        self.assertEqual(first_Element([], 5, 1), -1)
