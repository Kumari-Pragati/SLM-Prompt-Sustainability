import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_power_sum_with_positive_integer(self):
        self.assertEqual(even_Power_Sum(1), 1)
        self.assertEqual(even_Power_Sum(2), 8)
        self.assertEqual(even_Power_Sum(3), 28)
        self.assertEqual(even_Power_Sum(4), 64)
        self.assertEqual(even_Power_Sum(5), 128)
        self.assertEqual(even_Power_Sum(6), 216)
        self.assertEqual(even_Power_Sum(7), 344)
        self.assertEqual(even_Power_Sum(8), 512)
        self.assertEqual(even_Power_Sum(9), 728)
        self.assertEqual(even_Power_Sum(10), 1024)

    def test_even_power_sum_with_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_even_power_sum_with_negative_integer(self):
        self.assertEqual(even_Power_Sum(-1), 0)
        self.assertEqual(even_Power_Sum(-2), 0)
        self.assertEqual(even_Power_Sum(-3), 0)
        self.assertEqual(even_Power_Sum(-4), 0)
        self.assertEqual(even_Power_Sum(-5), 0)
        self.assertEqual(even_Power_Sum(-6), 0)
        self.assertEqual(even_Power_Sum(-7), 0)
        self.assertEqual(even_Power_Sum(-8), 0)
        self.assertEqual(even_Power_Sum(-9), 0)
        self.assertEqual(even_Power_Sum(-10), 0)
