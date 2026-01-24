import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_non_integer_string(self):
        self.assertFalse(check_integer("abc"))

    def test_positive_integer(self):
        self.assertTrue(check_integer("+123"))

    def test_negative_integer(self):
        self.assertTrue(check_integer("-123"))

    def test_integer_with_leading_zero(self):
        self.assertTrue(check_integer("0123"))

    def test_integer_with_leading_plus(self):
        self.assertTrue(check_integer("+0123"))

    def test_integer_with_leading_minus(self):
        self.assertTrue(check_integer("-0123"))

    def test_integer_with_leading_plus_and_zero(self):
        self.assertTrue(check_integer("+000123"))

    def test_integer_with_leading_minus_and_zero(self):
        self.assertTrue(check_integer("-000123"))

    def test_non_integer_string_with_leading_plus(self):
        self.assertFalse(check_integer("+abc"))

    def test_non_integer_string_with_leading_minus(self):
        self.assertFalse(check_integer("-abc"))

    def test_non_integer_string_with_leading_zero(self):
        self.assertFalse(check_integer("0abc"))

    def test_non_integer_string_with_leading_plus_and_zero(self):
        self.assertFalse(check_integer("+0abc"))

    def test_non_integer_string_with_leading_minus_and_zero(self):
        self.assertFalse(check_integer("-0abc"))
