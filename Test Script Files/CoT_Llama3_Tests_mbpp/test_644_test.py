import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(reverse_Array_Upto_K('hello', 2), 'lohel')

    def test_edge_case_k_zero(self):
        self.assertEqual(reverse_Array_Upto_K('hello', 0), 'hello')

    def test_edge_case_k_equal_to_length(self):
        self.assertEqual(reverse_Array_Upto_K('hello', 5), 'olleh')

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(reverse_Array_Upto_K('hello', 6), 'hello')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            reverse_Array_Upto_K(123, 2)

    def test_invalid_input_non_integer_k(self):
        with self.assertRaises(TypeError):
            reverse_Array_Upto_K('hello', 'a')

    def test_invalid_input_k_less_than_zero(self):
        with self.assertRaises(ValueError):
            reverse_Array_Upto_K('hello', -1)
