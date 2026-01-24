import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_small_prime(self):
        self.assertEqual(sum_of_odd_Factors(3), 3)

    def test_small_composite(self):
        self.assertEqual(sum_of_odd_Factors(12), 13)

    def test_large_prime(self):
        self.assertEqual(sum_of_odd_Factors(23), 23)

    def test_large_composite(self):
        self.assertEqual(sum_of_odd_Factors(36), 37)

    def test_edge_case_one(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_edge_case_two(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)

    def test_edge_case_sqrt(self):
        self.assertEqual(sum_of_odd_Factors(9), 10)

    def test_edge_case_sqrt_half(self):
        self.assertEqual(sum_of_odd_Factors(8), 9)

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            sum_of_odd_Factors(-1)

    def test_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            sum_of_odd_Factors(0)
