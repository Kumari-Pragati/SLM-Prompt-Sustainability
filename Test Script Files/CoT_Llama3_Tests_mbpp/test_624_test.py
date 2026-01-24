import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(is_upper("UPPER"))
    def test_lower(self):
        self.assertFalse(is_upper("lower"))
    def test_mixed(self):
        self.assertTrue(is_upper("UpPeR"))
    def test_empty(self):
        self.assertFalse(is_upper(""))
    def test_spaces(self):
        self.assertFalse(is_upper("   "))
    def test_numbers(self):
        self.assertFalse(is_upper("123"))
    def test_special_chars(self):
        self.assertFalse(is_upper("!@#"))
