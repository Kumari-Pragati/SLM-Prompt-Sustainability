import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertTrue(is_lower('hello'))
        self.assertTrue(is_lower('world'))
        self.assertTrue(is_lower('abc'))
        self.assertTrue(is_lower('xyz'))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(is_lower(''))
        self.assertTrue(is_lower('abcABC'))
        self.assertTrue(is_lower('123456'))
        self.assertTrue(is_lower('!@#$%^&*()'))

    def test_special_and_corner_cases(self):
        self.assertFalse(is_lower('HELLO'))
        self.assertFalse(is_lower('WORLD'))
        self.assertFalse(is_lower('ABC'))
        self.assertFalse(is_lower('XYZ'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_lower(123)
        with self.assertRaises(TypeError):
            is_lower([1, 2, 3])
