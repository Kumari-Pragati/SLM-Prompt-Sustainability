import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_base_case(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)

    def test_small_positive_numbers(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.3333333333333333)

    def test_large_positive_numbers(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.909090909090909)
        self.assertAlmostEqual(harmonic_sum(100), 5.151515151515151)

    def test_negative_numbers(self):
        self.assertAlmostEqual(harmonic_sum(-1), -1)
        self.assertRaises(ValueError, harmonic_sum, 0)
