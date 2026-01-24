import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertTrue(check_integer("123456"))

    def test_negative_integer(self):
        self.assertTrue(check_integer("-123456"))

    def test_positive_integer_with_spaces(self):
        self.assertTrue(check_integer("  123456  "))

    def test_negative_integer_with_spaces(self):
        self.assertTrue(check_integer("  -123456  "))

    def test_positive_integer_with_plus(self):
        self.assertTrue(check_integer("+123456"))

    def test_negative_integer_with_plus(self):
        self.assertFalse(check_integer("+-123456"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_string_with_non_digits(self):
        self.assertFalse(check_integer("123abc"))

    def test_string_with_single_digit(self):
        self.assertTrue(check_integer("5"))

    def test_string_with_single_negative_digit(self):
        self.assertFalse(check_integer("-5"))

    def test_string_with_single_plus_digit(self):
        self.assertFalse(check_integer("+5"))
