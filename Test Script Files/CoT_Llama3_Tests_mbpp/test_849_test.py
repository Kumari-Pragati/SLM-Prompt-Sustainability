import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_sum_of_primes(self):
        self.assertEqual(Sum(10), 8)

    def test_sum_of_primes_edge_case(self):
        self.assertEqual(Sum(2), 0)

    def test_sum_of_primes_edge_case2(self):
        self.assertEqual(Sum(1), 0)

    def test_sum_of_primes_invalid_input(self):
        with self.assertRaises(TypeError):
            Sum("a")

    def test_sum_of_primes_invalid_input2(self):
        with self.assertRaises(TypeError):
            Sum(-1)

    def test_sum_of_primes_invalid_input3(self):
        with self.assertRaises(TypeError):
            Sum(None)
