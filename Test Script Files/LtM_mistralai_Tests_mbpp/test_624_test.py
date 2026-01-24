import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_simple_uppercase(self):
        self.assertTrue(is_upper("HELLO"))

    def test_simple_lowercase(self):
        self.assertFalse(is_upper("hello"))

    def test_empty_string(self):
        self.assertFalse(is_upper(""))

    def test_single_uppercase_letter(self):
        self.assertTrue(is_upper("A"))

    def test_single_lowercase_letter(self):
        self.assertFalse(is_upper("a"))

    def test_mixed_case(self):
        self.assertFalse(is_upper("HeLlOwOrLd"))

    def test_special_characters(self):
        self.assertFalse(is_upper("!@#$%^&*()_+-=[]{}|;:'\",.<>/?"))
