import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Prime_Factors(100), 5)

    def test_edge_case(self):
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(3), 3)
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(9), 3)
        self.assertEqual(max_Prime_Factors(25), 5)

    def test_edge_case_with_large_number(self):
        self.assertEqual(max_Prime_Factors(1000000), 7)

    def test_edge_case_with_prime_number(self):
        self.assertEqual(max_Prime_Factors(23), 23)

    def test_edge_case_with_composite_number(self):
        self.assertEqual(max_Prime_Factors(36), 3)

    def test_edge_case_with_one(self):
        self.assertEqual(max_Prime_Factors(1), 1)

    def test_edge_case_with_zero(self):
        self.assertEqual(max_Prime_Factors(0), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_Prime_Factors('a')
