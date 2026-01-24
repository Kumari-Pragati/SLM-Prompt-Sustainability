import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_sqrt_root_positive(self):
        self.assertAlmostEqual(sqrt_root(9), 3.0)

    def test_sqrt_root_negative(self):
        with self.assertRaises(ValueError):
            sqrt_root(-9)

    def test_sqrt_root_zero(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)

    def test_sqrt_root_non_numeric(self):
        with self.assertRaises(TypeError):
            sqrt_root('a')

    def test_sqrt_root_edge_case(self):
        self.assertAlmostEqual(sqrt_root(1), 1.0)
