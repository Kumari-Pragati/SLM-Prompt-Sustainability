import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_non_digit(self):
        self.assertFalse(check_integer("a"))
        self.assertFalse(check_integer("A"))
        self.assertFalse(check_integer("!"))
        self.assertFalse(check_integer(" "))

    def test_single_digit(self):
        self.assertTrue(check_integer("1"))
        self.assertTrue(check_integer("2"))
        self.assertTrue(check_integer("3"))
        self.assertTrue(check_integer("4"))
        self.assertTrue(check_integer("5"))
        self.assertTrue(check_integer("6"))
        self.assertTrue(check_integer("7"))
        self.assertTrue(check_integer("8"))
        self.assertTrue(check_integer("9"))
        self.assertTrue(check_integer("0"))

    def test_multiple_digits(self):
        self.assertTrue(check_integer("123"))
        self.assertTrue(check_integer("456"))
        self.assertTrue(check_integer("789"))
        self.assertTrue(check_integer("012"))
        self.assertTrue(check_integer("987654321"))

    def test_leading_non_digit(self):
        self.assertTrue(check_integer("+1"))
        self.assertTrue(check_integer("-1"))
        self.assertTrue(check_integer("-123"))
        self.assertTrue(check_integer("+456"))

    def test_leading_non_digit_multiple_digits(self):
        self.assertTrue(check_integer("+123"))
        self.assertTrue(check_integer("-456"))
        self.assertTrue(check_integer("-789"))
        self.assertTrue(check_integer("+012"))
