import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertTrue(check_integer("12345"))

    def test_negative_integer(self):
        self.assertTrue(check_integer("-12345"))

    def test_positive_with_leading_plus(self):
        self.assertTrue(check_integer("+12345"))

    def test_negative_with_leading_minus(self):
        self.assertTrue(check_integer("-12345"))

    def test_positive_integer_with_spaces(self):
        self.assertTrue(check_integer("  12345  "))

    def test_negative_integer_with_spaces(self):
        self.assertTrue(check_integer("  -12345  "))

    def test_positive_integer_with_leading_plus_and_spaces(self):
        self.assertTrue(check_integer("  +12345  "))

    def test_negative_integer_with_leading_minus_and_spaces(self):
        self.assertTrue(check_integer("  -12345  "))

    def test_non_integer_string(self):
        self.assertFalse(check_integer("123abc"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_digit_integer(self):
        self.assertTrue(check_integer("5"))

    def test_single_digit_negative_integer(self):
        self.assertTrue(check_integer("-5"))

    def test_single_digit_positive_integer_with_leading_plus(self):
        self.assertTrue(check_integer("+5"))

    def test_single_digit_negative_integer_with_leading_minus(self):
        self.assertTrue(check_integer("-5"))

    def test_single_digit_integer_with_spaces(self):
        self.assertTrue(check_integer("  5  "))

    def test_single_digit_negative_integer_with_spaces(self):
        self.assertTrue(check_integer("  -5  "))

    def test_single_digit_integer_with_leading_plus_and_spaces(self):
        self.assertTrue(check_integer("  +5  "))

    def test_single_digit_negative_integer_with_leading_minus_and_spaces(self):
        self.assertTrue(check_integer("  -5  "))
