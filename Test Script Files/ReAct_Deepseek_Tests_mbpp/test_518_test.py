import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0)
        self.assertAlmostEqual(sqrt_root(9), 3.0)
        self.assertAlmostEqual(sqrt_root(16), 4.0)

    def test_zero(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            sqrt_root(-4)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sqrt_root('four')
