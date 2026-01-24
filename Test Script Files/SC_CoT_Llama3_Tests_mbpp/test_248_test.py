import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_typical(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.9289682539682539)

    def test_edge_case1(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_edge_case2(self):
        self.assertEqual(harmonic_sum(2), 1.5)

    def test_edge_case3(self):
        self.assertAlmostEqual(harmonic_sum(3), 1.5)

    def test_edge_case4(self):
        self.assertAlmostEqual(harmonic_sum(4), 1.8333333333333333)

    def test_edge_case5(self):
        self.assertAlmostEqual(harmonic_sum(5), 1.8333333333333333)

    def test_edge_case6(self):
        self.assertAlmostEqual(harmonic_sum(6), 2.0)

    def test_edge_case7(self):
        self.assertAlmostEqual(harmonic_sum(7), 1.9166666666666667)

    def test_edge_case8(self):
        self.assertAlmostEqual(harmonic_sum(8), 1.9375)

    def test_edge_case9(self):
        self.assertAlmostEqual(harmonic_sum(9), 1.9666666666666667)

    def test_edge_case10(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.0)

    def test_invalid_input(self):
        with self.assertRaises(ZeroDivisionError):
            harmonic_sum(0)
