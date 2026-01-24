import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_simple_lowercase(self):
        self.assertTrue(is_lower("lowercase"))

    def test_simple_uppercase(self):
        self.assertFalse(is_lower("UPPERCASE"))

    def test_mixed_case(self):
        self.assertTrue(is_lower("MixedCase"))

    def test_empty_string(self):
        self.assertFalse(is_lower(""))

    def test_whitespace(self):
        self.assertTrue(is_lower("\t\n "))

    def test_special_characters(self):
        self.assertTrue(is_lower("!@#$%^&*()_+-=[]{}|;:'\",.<>/?"))
