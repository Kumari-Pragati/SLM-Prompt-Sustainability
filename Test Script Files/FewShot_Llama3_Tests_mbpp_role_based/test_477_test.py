import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_lower_string(self):
        self.assertTrue(is_lower("hello"))

    def test_upper_string(self):
        self.assertFalse(is_lower("HELLO"))

    def test_mixed_string(self):
        self.assertTrue(is_lower("HeLlO"))

    def test_empty_string(self):
        self.assertFalse(is_lower(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_lower(123)
