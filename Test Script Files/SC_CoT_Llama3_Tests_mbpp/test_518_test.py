import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(sqrt_root(9), 3.0)
        self.assertAlmostEqual(sqrt_root(16), 4.0)
        self.assertAlmostEqual(sqrt_root(25), 5.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)
        self.assertAlmostEqual(sqrt_root(1), 1.0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sqrt_root(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sqrt_root('a')

    def test_zero_input(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)
