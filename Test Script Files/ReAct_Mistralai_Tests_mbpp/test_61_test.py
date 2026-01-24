import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substrings("", 0), 0)

    def test_single_digit(self):
        for num in range(1, 10):
            self.assertEqual(count_Substrings(str(num), len(str(num))), 1)

    def test_multiple_digits(self):
        for num in range(10, 100):
            self.assertEqual(count_Substrings(str(num), len(str(num))), 1)

    def test_negative_number(self):
        self.assertRaises(ValueError, count_Substrings, "-123", 3)

    def test_zero_number(self):
        self.assertEqual(count_Substrings("0", 1), 1)
        self.assertEqual(count_Substrings("00", 2), 2)
        self.assertEqual(count_Substrings("000", 3), 3)

    def test_longer_string(self):
        self.assertRaises(ValueError, count_Substrings, "123456789", 10)

    def test_non_numeric_string(self):
        self.assertRaises(ValueError, count_Substrings, "abc123", 3)
        self.assertRaises(ValueError, count_Substrings, "123abc", 5)
