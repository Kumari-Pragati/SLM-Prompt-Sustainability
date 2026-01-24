import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_normal(self):
        self.assertAlmostEqual(harmonic_sum(3), 1.3333333333333333)
        self.assertAlmostEqual(harmonic_sum(10), 1.4034285714285714)
        self.assertAlmostEqual(harmonic_sum(20), 1.4785714285714286)

    def test_edge_cases(self):
        self.assertAlmostEqual(harmonic_sum(1), 1.0)
        self.assertAlmostEqual(harmonic_sum(2), 0.5)

    def test_boundary(self):
        self.assertAlmostEqual(harmonic_sum(0), 1.0)
        self.assertAlmostEqual(harmonic_sum(1000000), 1.0 / 1000000)
