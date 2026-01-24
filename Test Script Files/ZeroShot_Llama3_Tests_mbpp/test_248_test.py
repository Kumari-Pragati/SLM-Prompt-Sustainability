import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum_1(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_harmonic_sum_2(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_harmonic_sum_3(self):
        self.assertAlmostEqual(harmonic_sum(3), 1.5 + 1/3, places=5)

    def test_harmonic_sum_4(self):
        self.assertAlmostEqual(harmonic_sum(4), 1.5 + 1/2 + 1/3, places=5)

    def test_harmonic_sum_5(self):
        self.assertAlmostEqual(harmonic_sum(5), 1.5 + 1/2 + 1/3 + 1/4, places=5)

    def test_harmonic_sum_negative(self):
        with self.assertRaises(ValueError):
            harmonic_sum(-1)

    def test_harmonic_sum_zero(self):
        with self.assertRaises(ValueError):
            harmonic_sum(0)
