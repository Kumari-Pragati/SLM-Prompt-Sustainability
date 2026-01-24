import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum_1(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_harmonic_sum_2(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_harmonic_sum_edge_case(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.6174)

    def test_harmonic_sum_negative(self):
        with self.assertRaises(ZeroDivisionError):
            harmonic_sum(-1)

    def test_harmonic_sum_zero(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_harmonic_sum_large(self):
        self.assertAlmostEqual(harmonic_sum(100), 5.18508)
