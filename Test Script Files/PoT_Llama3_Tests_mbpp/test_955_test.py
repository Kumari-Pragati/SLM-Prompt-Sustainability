import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(15))
        self.assertTrue(is_abundant(24))
        self.assertFalse(is_abundant(25))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(2))
        self.assertTrue(is_abundant(6))
        self.assertFalse(is_abundant(7))

    def test_corner_cases(self):
        self.assertFalse(is_abundant(0))
        self.assertFalse(is_abundant(3))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_abundant('a')
        with self.assertRaises(TypeError):
            is_abundant(None)
