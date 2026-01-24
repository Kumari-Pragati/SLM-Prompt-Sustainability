import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substrings('1234', 4), 3)

    def test_edge_case_single_digit(self):
        self.assertEqual(count_Substrings('1', 1), 0)

    def test_edge_case_all_same_digits(self):
        self.assertEqual(count_Substrings('1111', 4), 6)

    def test_edge_case_all_different_digits(self):
        self.assertEqual(count_Substrings('1234', 4), 3)

    def test_boundary_case_empty_string(self):
        self.assertEqual(count_Substrings('', 0), 0)

    def test_special_case_large_number(self):
        self.assertEqual(count_Substrings('1234567890'*1000, 10000), 1500500)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            count_Substrings(1234, 4)

    def test_invalid_input_string_with_non_digit_chars(self):
        with self.assertRaises(ValueError):
            count_Substrings('1234a', 5)
