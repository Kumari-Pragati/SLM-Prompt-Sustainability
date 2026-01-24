import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_power_sum_with_positive_numbers(self):
        self.assertEqual(even_Power_Sum(1), 8)
        self.assertEqual(even_Power_Sum(2), 88)
        self.assertEqual(even_Power_Sum(3), 2336)
        self.assertEqual(even_Power_Sum(4), 61608)
        self.assertEqual(even_Power_Sum(5), 1972808)

    def test_even_power_sum_with_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_even_power_sum_with_negative_numbers(self):
        self.assertEqual(even_Power_Sum(-1), 0)
        self.assertEqual(even_Power_Sum(-2), 0)
        self.assertEqual(even_Power_Sum(-3), 0)
        self.assertEqual(even_Power_Sum(-4), 0)
        self.assertEqual(even_Power_Sum(-5), 0)
