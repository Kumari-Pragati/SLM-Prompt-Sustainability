import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(harmonic_sum(1), 1)
        self.assertEqual(harmonic_sum(2), 1.5)
        self.assertEqual(harmonic_sum(3), 1.8333333333333333)

    def test_edge(self):
        self.assertEqual(harmonic_sum(0), 1)
        self.assertEqual(harmonic_sum(-1), 1)

    def test_negative(self):
        self.assertEqual(harmonic_sum(-2), 1.5)
        self.assertEqual(harmonic_sum(-3), 1.8333333333333333)

    def test_large(self):
        self.assertEqual(harmonic_sum(100), 6.283185307179586)

    def test_zero(self):
        self.assertEqual(harmonic_sum(0), 1)
