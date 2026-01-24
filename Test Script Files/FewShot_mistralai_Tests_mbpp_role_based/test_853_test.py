import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_of_odd_Factors(15), 41)

    def test_even_number(self):
        self.assertEqual(sum_of_odd_Factors(12), 24)

    def test_prime_number(self):
        self.assertEqual(sum_of_odd_Factors(5), 5)

    def test_square_number(self):
        self.assertEqual(sum_of_odd_Factors(9), 24)

    def test_small_number(self):
        self.assertEqual(sum_of_odd_Factors(3), 3)

    def test_large_number(self):
        self.assertEqual(sum_of_odd_Factors(1000001), 1000001)

    def test_negative_number(self):
        self.assertRaises(ValueError, sum_of_odd_Factors, -1)
