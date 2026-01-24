import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.3333333333333333)
        self.assertAlmostEqual(harmonic_sum(4), 1.25)
        self.assertAlmostEqual(harmonic_sum(5), 1.2)

    def test_edge_cases(self):
        self.assertAlmostEqual(harmonic_sum(0), 1)
        self.assertAlmostEqual(harmonic_sum(1e6), 1 + 1 / 1e6)
