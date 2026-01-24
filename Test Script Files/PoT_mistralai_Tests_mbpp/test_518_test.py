import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(sqrt_root(4), 2)
        self.assertAlmostEqual(sqrt_root(9), 3)
        self.assertAlmostEqual(sqrt_root(25), 5)

    def test_edge_and_boundary_cases(self):
        self.assertAlmostEqual(sqrt_root(0), 0)
        self.assertAlmostEqual(sqrt_root(1), 1)
        self.assertAlmostEqual(sqrt_root(16), 4)
        self.assertAlmostEqual(sqrt_root(2), 1.4142135623730951)
        self.assertAlmostEqual(sqrt_root(1024), 32)
