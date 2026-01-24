import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0)
        self.assertAlmostEqual(sqrt_root(9), 3.0)
        self.assertAlmostEqual(sqrt_root(16), 4.0)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)
        self.assertAlmostEqual(sqrt_root(1), 1.0)
        self.assertAlmostEqual(sqrt_root(0.25), 0.5)

    def test_corner_cases(self):
        self.assertAlmostEqual(sqrt_root(0.0001), 0.01)
        self.assertAlmostEqual(sqrt_root(0.01), 0.1)
        self.assertAlmostEqual(sqrt_root(10000), 100.0)
