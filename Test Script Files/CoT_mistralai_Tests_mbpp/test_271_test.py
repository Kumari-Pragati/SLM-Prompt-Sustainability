import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_even_power_sum_positive(self):
        self.assertEqual(even_Power_Sum(1), 1)
        self.assertEqual(even_Power_Sum(2), 8)
        self.assertEqual(even_Power_Sum(3), 28)
        self.assertEqual(even_Power_Sum(4), 64)
        self.assertEqual(even_Power_Sum(5), 128)
        self.assertEqual(even_Power_Sum(6), 256)
        self.assertEqual(even_Power_Sum(7), 512)
        self.assertEqual(even_Power_Sum(8), 1024)
        self.assertEqual(even_Power_Sum(9), 2048)

    def test_even_power_sum_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_even_power_sum_large_number(self):
        self.assertEqual(even_Power_Sum(1000), 16777216)

    def test_even_power_sum_negative(self):
        self.assertEqual(even_Power_Sum(-1), 0)
