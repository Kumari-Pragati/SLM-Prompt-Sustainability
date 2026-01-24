import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_power_sum_positive_numbers(self):
        self.assertEqual(even_Power_Sum(1), 1)
        self.assertEqual(even_Power_Sum(2), 8)
        self.assertEqual(even_Power_Sum(4), 1024)
        self.assertEqual(even_Power_Sum(6), 1028 + 1024 + 64)
        self.assertEqual(even_Power_Sum(8), 1028 + 1024 + 64 + 8)
        self.assertEqual(even_Power_Sum(10), 1028 + 1024 + 64 + 8 + 1024)

    def test_even_power_sum_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_even_power_sum_negative_numbers(self):
        self.assertEqual(even_Power_Sum(-1), 0)
        self.assertEqual(even_Power_Sum(-2), 0)
        self.assertEqual(even_Power_Sum(-4), 0)
        self.assertEqual(even_Power_Sum(-6), 0)
        self.assertEqual(even_Power_Sum(-8), 0)
        self.assertEqual(even_Power_Sum(-10), 0)

    def test_even_power_sum_large_numbers(self):
        self.assertEqual(even_Power_Sum(1000000), # Large positive number
                         sum([(2*i)*(2*i)*(2*i)*(2*i)*(2*i) for i in range(1, 1000001, 2)]))
