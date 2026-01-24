import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_sqrt_normal(self):
        self.assertAlmostEqual(sqrt_root(4), 2)
        self.assertAlmostEqual(sqrt_root(9), 3)
        self.assertAlmostEqual(sqrt_root(25), 5)

    def test_sqrt_edge_cases(self):
        self.assertAlmostEqual(sqrt_root(0), 0)
        self.assertAlmostEqual(sqrt_root(1), 1)

    def test_sqrt_boundary_cases(self):
        self.assertAlmostEqual(sqrt_root(2), 1.4142135623730951)
        self.assertAlmostEqual(sqrt_root(3), 1.7320508075688772)

    def test_sqrt_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sqrt_root(-1)
        with self.assertRaises(ValueError):
            sqrt_root(math.nan)
        with self.assertRaises(ValueError):
            sqrt_root(math.inf)
