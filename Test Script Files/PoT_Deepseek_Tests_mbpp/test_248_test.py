import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(harmonic_sum(0), 1)
        self.assertAlmostEqual(harmonic_sum(10), 2.9289682539682538)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            harmonic_sum('a')
        with self.assertRaises(ValueError):
            harmonic_sum(-1)
