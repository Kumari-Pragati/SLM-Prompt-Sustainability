import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(sqrt_root(4), 2)
        self.assertAlmostEqual(sqrt_root(9), 3)
        self.assertAlmostEqual(sqrt_root(25), 5)

    def test_zero(self):
        self.assertAlmostEqual(sqrt_root(0), 0)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            sqrt_root(-1)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            sqrt_root('string')

        with self.assertRaises(TypeError):
            sqrt_root(None)
