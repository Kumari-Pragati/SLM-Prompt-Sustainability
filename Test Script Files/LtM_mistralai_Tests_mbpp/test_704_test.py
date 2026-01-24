import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(harmonic_sum(1), 1)
        self.assertEqual(harmonic_sum(2), 1.5)

    def test_edge_cases(self):
        self.assertEqual(harmonic_sum(0), 1)
        self.assertEqual(harmonic_sum(3), 1.3333333333333333)

    def test_complex(self):
        self.assertAlmostEqual(harmonic_sum(100), 6.449489742783178)
        self.assertAlmostEqual(harmonic_sum(1000), 5.176388888888889)
