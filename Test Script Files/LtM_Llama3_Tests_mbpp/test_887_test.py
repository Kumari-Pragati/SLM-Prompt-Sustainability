import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_odd(1))
        self.assertFalse(is_odd(2))

    def test_edge(self):
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(3))

    def test_boundary(self):
        self.assertFalse(is_odd(10))
        self.assertTrue(is_odd(-10))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            is_odd('a')
