import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):

    def test_sqrt_root_simple(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0)
        self.assertAlmostEqual(sqrt_root(9), 3.0)

    def test_sqrt_root_edge(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)
        self.assertAlmostEqual(sqrt_root(1), 1.0)

    def test_sqrt_root_boundary(self):
        self.assertAlmostEqual(sqrt_root(math.pow(2, 31)), math.pow(2, 15))
        self.assertAlmostEqual(sqrt_root(math.pow(2, 63)), math.pow(2, 31))

    def test_sqrt_root_complex(self):
        self.assertAlmostEqual(sqrt_root(math.pow(10, 6)), math.pow(10, 3))
        self.assertAlmostEqual(sqrt_root(math.pow(2, 100)), math.pow(2, 50))
