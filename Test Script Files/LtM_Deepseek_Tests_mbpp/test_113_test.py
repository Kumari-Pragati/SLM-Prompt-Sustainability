import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_simple_positive_integer(self):
        self.assertTrue(check_integer("1234567890"))

    def test_simple_negative_integer(self):
        self.assertTrue(check_integer("-1234567890"))

    def test_simple_positive_integer_with_plus(self):
        self.assertTrue(check_integer("+1234567890"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_digit_integer(self):
        self.assertTrue(check_integer("5"))

    def test_single_digit_negative_integer(self):
        self.assertTrue(check_integer("-5"))

    def test_single_digit_positive_integer_with_plus(self):
        self.assertTrue(check_integer("+5"))

    def test_integer_with_leading_and_trailing_spaces(self):
        self.assertTrue(check_integer(" 123456 "))

    def test_integer_with_leading_and_trailing_spaces_and_plus(self):
        self.assertTrue(check_integer(" +123456 "))

    def test_integer_with_leading_and_trailing_spaces_and_minus(self):
        self.assertTrue(check_integer(" -123456 "))

    def test_integer_with_non_numeric_characters(self):
        self.assertFalse(check_integer("123abc"))

    def test_integer_with_numeric_and_non_numeric_characters(self):
        self.assertFalse(check_integer("123abc456"))

    def test_integer_with_leading_plus_and_non_numeric_characters(self):
        self.assertFalse(check_integer("+123abc"))

    def test_integer_with_leading_minus_and_non_numeric_characters(self):
        self.assertFalse(check_integer("-123abc"))
