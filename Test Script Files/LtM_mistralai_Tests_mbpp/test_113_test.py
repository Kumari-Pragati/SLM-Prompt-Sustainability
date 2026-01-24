import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_simple_positive_integer(self):
        self.assertTrue(check_integer("12345"))

    def test_simple_negative_integer(self):
        self.assertTrue(check_integer("-12345"))

    def test_single_digit(self):
        self.assertTrue(check_integer("7"))

    def test_zero(self):
        self.assertTrue(check_integer("0"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_leading_plus_or_minus(self):
        self.assertTrue(check_integer("+12345"))
        self.assertTrue(check_integer("-12345"))

    def test_leading_zero(self):
        self.assertTrue(check_integer("012345"))

    def test_long_integer(self):
        self.assertTrue(check_integer("123456789012345"))

    def test_invalid_characters(self):
        self.assertFalse(check_integer("1a2345"))
        self.assertFalse(check_integer("12345x"))
        self.assertFalse(check_integer("12345A"))
