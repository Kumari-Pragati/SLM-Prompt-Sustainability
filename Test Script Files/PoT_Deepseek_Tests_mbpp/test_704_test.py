import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333)

    def test_edge_cases(self):
        self.assertEqual(harmonic_sum(0), 1)
        self.assertEqual(harmonic_sum(-1), 1)

    def test_boundary_cases(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.9289682539682538)
        self.assertAlmostEqual(harmonic_sum(100), 5.18737751763966)
