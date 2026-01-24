import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_positive_integer(self):
        self.assertTrue(check_integer("12345"))
        self.assertTrue(check_integer("0"))
        self.assertTrue(check_integer("987654321"))

    def test_negative_integer(self):
        self.assertTrue(check_integer("-12345"))
        self.assertTrue(check_integer("-0"))
        self.assertTrue(check_integer("-987654321"))

    def test_zero(self):
        self.assertTrue(check_integer("+0"))
        self.assertTrue(check_integer("-0"))
        self.assertTrue(check_integer("0"))

    def test_single_non_numeric_char(self):
        self.assertFalse(check_integer("1a234"))
        self.assertFalse(check_integer("123a4"))
        self.assertFalse(check_integer("1234a"))

    def test_multiple_non_numeric_chars(self):
        self.assertFalse(check_integer("1a2b34"))
        self.assertFalse(check_integer("123a4b"))
        self.assertFalse(check_integer("1234a5b"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_char(self):
        for char in "!@#$%^&*()_+-=[]{}|;:'\",.<>?0123456789":
            self.assertIsNone(check_integer(char))
