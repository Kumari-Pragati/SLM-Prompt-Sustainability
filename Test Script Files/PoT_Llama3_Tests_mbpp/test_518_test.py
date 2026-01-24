import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(sqrt_root(9), 3.0)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(sqrt_root(0), 0.0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            sqrt_root(-1)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            sqrt_root('a')

    def test_edge_case_complex(self):
        with self.assertRaises(TypeError):
            sqrt_root(1+2j)

    def test_edge_case_infinity(self):
        with self.assertRaises(OverflowError):
            sqrt_root(float('inf'))

    def test_edge_case_negative_infinity(self):
        with self.assertRaises(OverflowError):
            sqrt_root(float('-inf'))
