import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('11111', 5), 5)

    def test_edge_case_zero_length_string(self):
        self.assertEqual(odd_Equivalent('', 5), 0)

    def test_edge_case_zero_length_input(self):
        self.assertEqual(odd_Equivalent('11111', 0), 0)

    def test_edge_case_single_digit_string(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_string_zero_length_input(self):
        self.assertEqual(odd_Equivalent('1', 0), 0)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            odd_Equivalent('11111', 'five')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            odd_Equivalent(123, 5)
