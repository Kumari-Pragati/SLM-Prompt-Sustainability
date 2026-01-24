import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_uppercase_string(self):
        self.assertTrue(is_upper("UPPERCASE"))

    def test_lowercase_string(self):
        self.assertFalse(is_upper("lowercase"))

    def test_mixedcase_string(self):
        self.assertTrue(is_upper("MixedCase"))

    def test_empty_string(self):
        self.assertFalse(is_upper(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_upper(123)
