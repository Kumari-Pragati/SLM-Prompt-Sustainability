import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_lowercase_string(self):
        self.assertTrue(is_lower("lowercase"))

    def test_mixed_case_string(self):
        self.assertTrue(is_lower("mixedCase"))

    def test_uppercase_string(self):
        self.assertFalse(is_lower("UPPERCASE"))

    def test_empty_string(self):
        self.assertTrue(is_lower(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_lower(123)
