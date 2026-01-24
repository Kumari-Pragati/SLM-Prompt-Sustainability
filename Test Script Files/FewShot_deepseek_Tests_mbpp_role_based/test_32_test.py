import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_Prime_Factors(315), 7)

    def test_edge_case(self):
        self.assertEqual(max_Prime_Factors(2), 2)

    def test_boundary_case(self):
        self.assertEqual(max_Prime_Factors(1), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_Prime_Factors("abc")

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            max_Prime_Factors(-10)
