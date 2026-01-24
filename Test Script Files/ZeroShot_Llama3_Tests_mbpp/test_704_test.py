import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum(self):
        self.assertAlmostEqual(harmonic_sum(1), 1, places=6)
        self.assertAlmostEqual(harmonic_sum(2), 1.5, places=6)
        self.assertAlmostEqual(harmonic_sum(3), 1.6666666666666667, places=6)
        self.assertAlmostEqual(harmonic_sum(4), 1.8333333333333333, places=6)
        self.assertAlmostEqual(harmonic_sum(5), 1.9166666666666667, places=6)
        self.assertAlmostEqual(harmonic_sum(10), 2.9289682539682538, places=6)
        self.assertAlmostEqual(harmonic_sum(20), 3.8494824248494824, places=6)
        self.assertAlmostEqual(harmonic_sum(50), 4.444444444444444, places=6)
        self.assertAlmostEqual(harmonic_sum(100), 5.185185185185185, places=6)

    def test_harmonic_sum_edge_cases(self):
        self.assertEqual(harmonic_sum(0), 1)
        self.assertEqual(harmonic_sum(1), 1)
        self.assertEqual(harmonic_sum(2), 1.5)
