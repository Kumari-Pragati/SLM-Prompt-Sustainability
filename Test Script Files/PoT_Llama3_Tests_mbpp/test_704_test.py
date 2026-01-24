import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(harmonic_sum(5), 1.791466984544906)

    def test_edge_case_n_1(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)

    def test_edge_case_n_2(self):
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_edge_case_n_0(self):
        with self.assertRaises(ValueError):
            harmonic_sum(0)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            harmonic_sum(-1)

    def test_edge_case_n_non_integer(self):
        with self.assertRaises(TypeError):
            harmonic_sum(3.5)

    def test_edge_case_n_large(self):
        self.assertAlmostEqual(harmonic_sum(100), 2.253215990203161)
