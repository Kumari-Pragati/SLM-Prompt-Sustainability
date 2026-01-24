import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(harmonic_sum(0), 1)
        self.assertAlmostEqual(harmonic_sum(-1), 1)

    def test_complex_cases(self):
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333)
        self.assertAlmostEqual(harmonic_sum(4), 1.9166666666666667)
