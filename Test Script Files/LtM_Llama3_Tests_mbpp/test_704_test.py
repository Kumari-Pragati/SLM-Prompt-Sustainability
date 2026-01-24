import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(harmonic_sum(1), 1)
        self.assertEqual(harmonic_sum(2), 1.5)
        self.assertEqual(harmonic_sum(3), 1.8333333333333333)

    def test_edge(self):
        self.assertEqual(harmonic_sum(0), 1)
        self.assertEqual(harmonic_sum(-1), 1)

    def test_negative(self):
        self.assertEqual(harmonic_sum(-2), 1.5)
        self.assertEqual(harmonic_sum(-3), 1.8333333333333333)

    def test_large(self):
        self.assertAlmostEqual(harmonic_sum(100), 2.8333333333333335)
        self.assertAlmostEqual(harmonic_sum(200), 4.8333333333333335)
