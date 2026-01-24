import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Substrings("12345", 5), 2)

    def test_empty_string(self):
        self.assertEqual(count_Substrings("", 0), 1)

    def test_single_digit(self):
        self.assertEqual(count_Substrings("1", 1), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            count_Substrings("123", -1)

    def test_zero_length_input(self):
        with self.assertRaises(ValueError):
            count_Substrings("", 0)

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            count_Substrings("abc", 10)
