import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(harmonic_sum(5), 1.2766)

    def test_zero(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_negative_integer(self):
        self.assertRaises(ValueError, harmonic_sum, -1)

    def test_fraction(self):
        self.assertRaises(TypeError, harmonic_sum, 3.14)

    def test_non_number(self):
        self.assertRaises(TypeError, harmonic_sum, 'string')
