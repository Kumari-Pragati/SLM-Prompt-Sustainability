import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_integer("12345"))

    def test_with_plus_sign(self):
        self.assertTrue(check_integer("+12345"))

    def test_with_minus_sign(self):
        self.assertTrue(check_integer("-12345"))

    def test_with_leading_and_trailing_spaces(self):
        self.assertTrue(check_integer(" 12345 "))

    def test_with_plus_and_spaces(self):
        self.assertTrue(check_integer("+ 12345"))

    def test_with_minus_and_spaces(self):
        self.assertTrue(check_integer("- 12345"))

    def test_with_non_integer_characters(self):
        self.assertFalse(check_integer("12345a"))

    def test_with_non_numeric_characters(self):
        self.assertFalse(check_integer("+12345a"))

    def test_with_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_with_single_digit(self):
        self.assertTrue(check_integer("5"))

    def test_with_single_sign(self):
        self.assertIsNone(check_integer("+"))
        self.assertIsNone(check_integer("-"))
