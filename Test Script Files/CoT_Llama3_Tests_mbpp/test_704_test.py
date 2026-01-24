import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum_positive(self):
        self.assertAlmostEqual(harmonic_sum(1), 1, places=6)
        self.assertAlmostEqual(harmonic_sum(2), 1.5, places=6)
        self.assertAlmostEqual(harmonic_sum(3), 1.833333, places=6)
        self.assertAlmostEqual(harmonic_sum(4), 2.083333, places=6)
        self.assertAlmostEqual(harmonic_sum(5), 2.283333, places=6)

    def test_harmonic_sum_negative(self):
        with self.assertRaises(ValueError):
            harmonic_sum(-1)

    def test_harmonic_sum_zero(self):
        self.assertAlmostEqual(harmonic_sum(0), 1, places=6)

    def test_harmonic_sum_one(self):
        self.assertAlmostEqual(harmonic_sum(1), 1, places=6)

    def test_harmonic_sum_large(self):
        self.assertAlmostEqual(harmonic_sum(100), 5.185567, places=6)
