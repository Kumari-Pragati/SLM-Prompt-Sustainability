import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.9289682539682539)

    def test_edge_case_n_1(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)

    def test_edge_case_n_2(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_edge_case_n_0(self):
        self.assertAlmostEqual(harmonic_sum(0), 1)

    def test_negative_input(self):
        with self.assertRaises(ZeroDivisionError):
            harmonic_sum(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            harmonic_sum(3.5)

    def test_large_input(self):
        self.assertAlmostEqual(harmonic_sum(100), 5.148713616413041)
