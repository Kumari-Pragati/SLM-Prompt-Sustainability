import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(end_num(""))

    def test_no_digits(self):
        self.assertFalse(end_num("abcdefg"))

    def test_single_digit(self):
        self.assertTrue(end_num("1"))

    def test_multiple_digits(self):
        self.assertTrue(end_num("12345"))

    def test_leading_digits(self):
        self.assertTrue(end_num("123456789"))

    def test_trailing_whitespace(self):
        self.assertTrue(end_num("123456789 "))

    def test_non_numeric_characters(self):
        self.assertFalse(end_num("1a2b3c4"))

    def test_negative_numbers(self):
        self.assertTrue(end_num("-123"))
