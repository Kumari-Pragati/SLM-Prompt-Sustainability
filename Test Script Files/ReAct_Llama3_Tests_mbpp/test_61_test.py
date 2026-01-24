import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substrings("", 0), 0)

    def test_single_digit(self):
        self.assertEqual(count_Substrings("1", 1), 1)

    def test_multiple_digits(self):
        self.assertEqual(count_Substrings("123", 3), 2)

    def test_zero_in_string(self):
        self.assertEqual(count_Substrings("012", 3), 1)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            count_Substrings("123", -1)

    def test_non_integer_string(self):
        with self.assertRaises(TypeError):
            count_Substrings("abc", 3)
