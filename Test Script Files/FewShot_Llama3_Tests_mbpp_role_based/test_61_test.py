import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Substrings("123", 3), 2)

    def test_edge_case_zero_length(self):
        self.assertEqual(count_Substrings("", 0), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(count_Substrings("1", 1), 1)

    def test_edge_case_multiple_digits(self):
        self.assertEqual(count_Substrings("123", 3), 2)

    def test_edge_case_negative_length(self):
        with self.assertRaises(ValueError):
            count_Substrings("123", -1)

    def test_edge_case_non_integer_length(self):
        with self.assertRaises(TypeError):
            count_Substrings("123", "abc")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            count_Substrings(123, 3)
