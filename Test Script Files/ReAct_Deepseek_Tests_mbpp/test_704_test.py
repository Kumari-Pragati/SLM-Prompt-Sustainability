import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum_typical_case(self):
        self.assertAlmostEqual(harmonic_sum(5), 2.28333410307, places=7)

    def test_harmonic_sum_edge_case(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_harmonic_sum_zero_case(self):
        with self.assertRaises(RecursionError):
            harmonic_sum(0)

    def test_harmonic_sum_negative_case(self):
        with self.assertRaises(RecursionError):
            harmonic_sum(-1)
