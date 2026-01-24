import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_positive_integer(self):
        self.assertTrue(check_integer("+1234567890"))

    def test_negative_integer(self):
        self.assertTrue(check_integer("-1234567890"))

    def test_single_digit_integer(self):
        self.assertTrue(check_integer("5"))

    def test_multiple_digits_integer(self):
        self.assertTrue(check_integer("1234567890"))

    def test_leading_zeroes(self):
        self.assertFalse(check_integer("00123"))

    def test_non_integer_string(self):
        self.assertFalse(check_integer("123abc"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_whitespace_string(self):
        self.assertIsNone(check_integer(" "))

    def test_single_char_string(self):
        self.assertFalse(check_integer("a"))
