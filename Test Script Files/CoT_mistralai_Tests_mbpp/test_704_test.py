import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_base_case(self):
        self.assertAlmostEqual(harmonic_sum(1), 1.0)

    def test_small_positive_integer(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.3333333333333333)

    def test_large_positive_integer(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.909090909090909)
        self.assertAlmostEqual(harmonic_sum(100), 50.505050505050504)

    def test_negative_input(self):
        self.assertRaises(ValueError, harmonic_sum, -1)

    def test_zero_input(self):
        self.assertRaises(ValueError, harmonic_sum, 0)

    def test_float_input(self):
        self.assertAlmostEqual(harmonic_sum(2.5), 1.25)
