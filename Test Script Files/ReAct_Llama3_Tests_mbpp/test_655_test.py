import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_fifth_power_sum_positive(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 32)
        self.assertEqual(fifth_Power_Sum(3), 288)
        self.assertEqual(fifth_Power_Sum(4), 2464)
        self.assertEqual(fifth_Power_Sum(5), 16128)

    def test_fifth_power_sum_negative(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum(-1)

    def test_fifth_power_sum_zero(self):
        self.assertEqual(fifth_Power_Sum(0), 0)

    def test_fifth_power_sum_large(self):
        self.assertEqual(fifth_Power_Sum(10), 43046721)
