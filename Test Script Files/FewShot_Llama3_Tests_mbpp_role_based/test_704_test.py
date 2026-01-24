import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_harmonic_sum_zero(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_harmonic_sum_one(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_harmonic_sum_two(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_harmonic_sum_three(self):
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333)

    def test_harmonic_sum_negative(self):
        with self.assertRaises(ValueError):
            harmonic_sum(-1)

    def test_harmonic_sum_non_integer(self):
        with self.assertRaises(TypeError):
            harmonic_sum(3.5)
