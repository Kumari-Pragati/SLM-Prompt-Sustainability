import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(harmonic_sum(5), 1.2320546492503131)
        self.assertAlmostEqual(harmonic_sum(10), 1.4014087407452623)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(harmonic_sum(1), 1.0)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.3333333333333333)
        self.assertAlmostEqual(harmonic_sum(100), 5.159571824175926)
        self.assertAlmostEqual(harmonic_sum(1000), 6.283185307179586)

    def test_invalid_input(self):
        self.assertRaises(TypeError, harmonic_sum, 'a')
        self.assertRaises(TypeError, harmonic_sum, -1)
        self.assertRaises(ValueError, harmonic_sum, 0)
