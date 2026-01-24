import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_simple_positive(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0)

    def test_simple_negative(self):
        self.assertAlmostEqual(sqrt_root(-4), 2.0j)

    def test_edge_zero(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)

    def test_edge_negative(self):
        self.assertAlmostEqual(sqrt_root(-1), 1j)

    def test_edge_positive(self):
        self.assertAlmostEqual(sqrt_root(1), 1.0)

    def test_edge_max(self):
        self.assertAlmostEqual(sqrt_root(2**31 - 1), 2**15.5)

    def test_edge_min(self):
        self.assertAlmostEqual(sqrt_root(-2**31), -2**15.5)

    def test_edge_max_negative(self):
        self.assertAlmostEqual(sqrt_root(-2**31), -2**15.5)

    def test_edge_min_negative(self):
        self.assertAlmostEqual(sqrt_root(-2**31 - 1), -2**15.5)
