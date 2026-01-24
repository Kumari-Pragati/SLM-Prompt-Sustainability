import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum_typical_case(self):
        self.assertAlmostEqual(harmonic_sum(5), 2.28333410307, places=7)

    def test_harmonic_sum_small_number(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_harmonic_sum_zero(self):
        with self.assertRaises(RecursionError):
            harmonic_sum(0)

    def test_harmonic_sum_negative_number(self):
        with self.assertRaises(RecursionError):
            harmonic_sum(-1)

    def test_harmonic_sum_large_number(self):
        self.assertAlmostEqual(harmonic_sum(100), 5.187377517638672, places=7)
