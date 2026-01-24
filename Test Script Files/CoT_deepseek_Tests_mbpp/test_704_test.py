import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333)
        self.assertAlmostEqual(harmonic_sum(4), 2.083333333333333)

    def test_large_numbers(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.9289682539682538)
        self.assertAlmostEqual(harmonic_sum(20), 3.4515056383838386)

    def test_boundary_conditions(self):
        self.assertEqual(harmonic_sum(0), 1)
        self.assertEqual(harmonic_sum(-1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            harmonic_sum('a')
        with self.assertRaises(TypeError):
            harmonic_sum(None)
        with self.assertRaises(TypeError):
            harmonic_sum(1.5)
