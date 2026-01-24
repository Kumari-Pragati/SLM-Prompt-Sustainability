import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_small_numbers(self):
        self.assertEqual(harmonic_sum(2), 1.5)
        self.assertEqual(harmonic_sum(3), 1.3333333333333333)

    def test_large_numbers(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.9000000000000003)
        self.assertAlmostEqual(harmonic_sum(100), 50.500000000000004)
        self.assertAlmostEqual(harmonic_sum(1000), 666.6666666666667)
