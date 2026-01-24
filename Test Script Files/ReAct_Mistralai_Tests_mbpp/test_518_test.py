import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0, delta=0.01)
        self.assertAlmostEqual(sqrt_root(9), 3.0, delta=0.01)

    def test_zero(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0, delta=0.01)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            sqrt_root(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sqrt_root('string')

    def test_large_numbers(self):
        self.assertAlmostEqual(sqrt_root(1e6), 1000.0, delta=10.0)
