import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_uppercase_string(self):
        self.assertTrue(is_upper("HELLO"))

    def test_mixed_case_string(self):
        self.assertFalse(is_upper("Hello"))

    def test_empty_string(self):
        self.assertFalse(is_upper(""))

    def test_whitespace_string(self):
        self.assertFalse(is_upper("   "))

    def test_special_characters_string(self):
        self.assertFalse(is_upper("!@#$%^&*()"))
