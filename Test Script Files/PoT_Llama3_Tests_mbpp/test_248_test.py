import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(harmonic_sum(1), 1, places=5)
        self.assertAlmostEqual(harmonic_sum(2), 1.5, places=5)
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333, places=5)
        self.assertAlmostEqual(harmonic_sum(4), 2.083333333333333, places=5)

    def test_edge_and_boundary_cases(self):
        self.assertAlmostEqual(harmonic_sum(0), 1, places=5)
        self.assertAlmostEqual(harmonic_sum(1), 1, places=5)
        self.assertAlmostEqual(harmonic_sum(2), 1.5, places=5)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(RecursionError):
            harmonic_sum(1000000)
