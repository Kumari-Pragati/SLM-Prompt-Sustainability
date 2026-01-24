import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_base_case(self):
        """Test base case: n = 1"""
        self.assertEqual(harmonic_sum(1), 1)

    def test_small_positive_integer(self):
        """Test small positive integers"""
        self.assertEqual(harmonic_sum(2), 1.5)
        self.assertEqual(harmonic_sum(3), 1.3333333333333333)

    def test_large_positive_integer(self):
        """Test large positive integers"""
        self.assertEqual(harmonic_sum(10), 2.909090909090909)
        self.assertEqual(harmonic_sum(100), 5.151515151515151)

    def test_negative_integer(self):
        """Test negative integer"""
        with self.assertRaises(ValueError):
            harmonic_sum(-1)

    def test_zero(self):
        """Test zero"""
        with self.assertRaises(ValueError):
            harmonic_sum(0)

    def test_floating_point(self):
        """Test floating point number"""
        self.assertAlmostEqual(harmonic_sum(2.5), 1.3888888888888889)
