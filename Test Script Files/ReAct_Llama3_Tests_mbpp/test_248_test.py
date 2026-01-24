import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_harmonic_sum_1(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_harmonic_sum_2(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_harmonic_sum_3(self):
        self.assertAlmostEqual(harmonic_sum(3), 1.5 + 1/3)

    def test_harmonic_sum_edge_case_1(self):
        with self.assertRaises(ZeroDivisionError):
            harmonic_sum(1)

    def test_harmonic_sum_edge_case_2(self):
        self.assertEqual(harmonic_sum(2), 1)
