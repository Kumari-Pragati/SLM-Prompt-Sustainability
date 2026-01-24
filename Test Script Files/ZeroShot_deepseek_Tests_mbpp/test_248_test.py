import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum_with_positive_numbers(self):
        self.assertAlmostEqual(harmonic_sum(1), 1.0)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333)
        self.assertAlmostEqual(harmonic_sum(4), 2.083333333333333)

    def test_harmonic_sum_with_zero(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_harmonic_sum_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            harmonic_sum(-1)
