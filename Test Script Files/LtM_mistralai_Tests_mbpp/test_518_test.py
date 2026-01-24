import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertAlmostEqual(sqrt_root(4), 2)
        self.assertAlmostEqual(sqrt_root(9), 3)
        self.assertAlmostEqual(sqrt_root(25), 5)

    def test_edge_cases(self):
        self.assertAlmostEqual(sqrt_root(0), 0)
        self.assertAlmostEqual(sqrt_root(1), 1)
        self.assertAlmostEqual(sqrt_root(16), 4)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, sqrt_root, -1)
        self.assertAlmostEqual(sqrt_root(-4), -2)

    def test_complex_numbers(self):
        self.assertAlmostEqual(sqrt_root(-16 + 0j), 4j)
        self.assertAlmostEqual(sqrt_root(-16 + 1j), (4 + 1j) / 2)
        self.assertAlmostEqual(sqrt_root(-16 + -1j), (4 - 1j) / 2)
