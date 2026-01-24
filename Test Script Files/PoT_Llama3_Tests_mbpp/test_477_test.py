import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_lower("hello"))
        self.assertTrue(is_lower("world"))
        self.assertTrue(is_lower("python"))

    def test_edge_cases(self):
        self.assertTrue(is_lower("HELLO"))
        self.assertTrue(is_lower("WORLD"))
        self.assertTrue(is_lower("PYTHON"))

    def test_empty_string(self):
        self.assertFalse(is_lower(""))

    def test_single_character(self):
        self.assertTrue(is_lower("a"))
        self.assertTrue(is_lower("z"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_lower(123)
