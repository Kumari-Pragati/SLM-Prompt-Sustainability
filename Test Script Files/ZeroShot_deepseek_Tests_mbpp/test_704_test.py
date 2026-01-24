import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_harmonic_sum_1(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_harmonic_sum_2(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_harmonic_sum_3(self):
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333)

    def test_harmonic_sum_4(self):
        self.assertAlmostEqual(harmonic_sum(4), 2.083333333333333)

    def test_harmonic_sum_5(self):
        self.assertAlmostEqual(harmonic_sum(5), 2.283333333333333)

    def test_harmonic_sum_6(self):
        self.assertAlmostEqual(harmonic_sum(6), 2.458333333333333)

    def test_harmonic_sum_7(self):
        self.assertAlmostEqual(harmonic_sum(7), 2.613888888888889)

    def test_harmonic_sum_8(self):
        self.assertAlmostEqual(harmonic_sum(8), 2.7546296296296297)

    def test_harmonic_sum_9(self):
        self.assertAlmostEqual(harmonic_sum(9), 2.885648148148148)

    def test_harmonic_sum_10(self):
        self.assertAlmostEqual(harmonic_sum(10), 3.010605263157895)
