import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_is_lower_string(self):
        self.assertTrue(is_lower("hello"))
        self.assertTrue(is_lower("world"))
        self.assertTrue(is_lower("Python"))

    def test_is_lower_empty_string(self):
        self.assertTrue(is_lower(""))

    def test_is_lower_uppercase_string(self):
        self.assertFalse(is_lower("HELLO"))
        self.assertFalse(is_lower("WORLD"))
        self.assertFalse(is_lower("PYTHON"))

    def test_is_lower_mixed_case_string(self):
        self.assertTrue(is_lower("HeLlo"))
        self.assertTrue(is_lower("wOrLd"))
        self.assertTrue(is_lower("PyThOn"))

    def test_is_lower_non_string_input(self):
        self.assertRaises(TypeError, is_lower, 123)
        self.assertRaises(TypeError, is_lower, [1, 2, 3])
        self.assertRaises(TypeError, is_lower, (1, 2, 3))
        self.assertRaises(TypeError, is_lower, None)
        self.assertRaises(TypeError, is_lower, {})
