import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(is_lower("hello"))
        self.assertTrue(is_lower("world"))
        self.assertTrue(is_lower("python"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_lower(""))
        self.assertTrue(is_lower("abc"))
        self.assertTrue(is_lower("ABC"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_lower(123)
        with self.assertRaises(TypeError):
            is_lower([1, 2, 3])

    def test_non_string_inputs(self):
        self.assertTrue(is_lower("hello world"))
        self.assertTrue(is_lower("   hello   "))
