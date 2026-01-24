import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_harmonic_sum_positive_integer(self):
        self.assertAlmostEqual(harmonic_sum(5), 1.6449340668482264)

    def test_harmonic_sum_zero(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_harmonic_sum_negative_integer(self):
        self.assertAlmostEqual(harmonic_sum(-5), 1.6449340668482264)

    def test_harmonic_sum_non_integer(self):
        with self.assertRaises(TypeError):
            harmonic_sum(3.5)
