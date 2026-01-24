import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0)

    def test_zero(self):
        self.assertEqual(sqrt_root(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt_root(-1)

    def test_large_number(self):
        self.assertAlmostEqual(sqrt_root(1e20), 1e10)

    def test_small_number(self):
        self.assertAlmostEqual(sqrt_root(1e-20), 1e-10)

    def test_float_number(self):
        self.assertAlmostEqual(sqrt_root(2.25), 1.5)
