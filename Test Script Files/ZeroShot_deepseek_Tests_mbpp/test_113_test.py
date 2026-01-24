import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_whitespace_string(self):
        self.assertIsNone(check_integer(" "))

    def test_single_digit(self):
        self.assertTrue(check_integer("5"))

    def test_multiple_digits(self):
        self.assertTrue(check_integer("1234567890"))

    def test_negative_number(self):
        self.assertTrue(check_integer("-1234567890"))

    def test_positive_number(self):
        self.assertTrue(check_integer("+1234567890"))

    def test_mixed_digits_and_whitespace(self):
        self.assertFalse(check_integer("1 2 3 4 5"))

    def test_mixed_digits_and_symbols(self):
        self.assertFalse(check_integer("1234567890!"))

    def test_mixed_digits_and_symbols_with_whitespace(self):
        self.assertFalse(check_integer("1234567890 !"))
