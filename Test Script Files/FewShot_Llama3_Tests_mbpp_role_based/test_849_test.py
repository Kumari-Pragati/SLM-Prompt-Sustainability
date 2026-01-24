import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_sum_of_prime_divisors_for_small_numbers(self):
        self.assertEqual(Sum(10), 8)

    def test_sum_of_prime_divisors_for_large_numbers(self):
        self.assertEqual(Sum(100), 44)

    def test_sum_of_prime_divisors_for_edge_case(self):
        self.assertEqual(Sum(2), 0)

    def test_sum_of_prime_divisors_for_invalid_input(self):
        with self.assertRaises(TypeError):
            Sum("invalid_input")
