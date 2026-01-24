import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Prime_Factors(315), 7)

    def test_edge_case_small_number(self):
        self.assertEqual(max_Prime_Factors(2), 2)

    def test_edge_case_large_number(self):
        self.assertEqual(max_Prime_Factors(10**18), 2)

    def test_edge_case_prime_number(self):
        self.assertEqual(max_Prime_Factors(13), 13)

    def test_edge_case_one(self):
        self.assertEqual(max_Prime_Factors(1), -1)

    def test_invalid_input_negative_number(self):
        with self.assertRaises(Exception):
            max_Prime_Factors(-10)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(Exception):
            max_Prime_Factors(10.5)
