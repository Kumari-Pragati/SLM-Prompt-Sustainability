import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_valid_integer(self):
        self.assertTrue(check_integer("123"))
        self.assertTrue(check_integer("456"))
        self.assertTrue(check_integer("-789"))
        self.assertTrue(check_integer("+890"))

    def test_invalid_integer(self):
        self.assertFalse(check_integer("abc"))
        self.assertFalse(check_integer("123abc"))
        self.assertFalse(check_integer("-abc"))
        self.assertFalse(check_integer("+abc"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_character(self):
        self.assertFalse(check_integer("a"))
        self.assertFalse(check_integer("1"))

    def test_multiple_characters(self):
        self.assertFalse(check_integer("abc"))
        self.assertFalse(check_integer("123abc"))

    def test_leading_plus_or_minus(self):
        self.assertTrue(check_integer("+123"))
        self.assertTrue(check_integer("-456"))

    def test_leading_plus_or_minus_invalid(self):
        self.assertFalse(check_integer("+abc"))
        self.assertFalse(check_integer("-abc"))
