import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_fourth_power_sum(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 16)
        self.assertEqual(fourth_Power_Sum(3), 81)
        self.assertEqual(fourth_Power_Sum(4), 256)
        self.assertEqual(fourth_Power_Sum(5), 625)
        self.assertEqual(fourth_Power_Sum(10), 4561)
        self.assertEqual(fourth_Power_Sum(20), 322560)
        self.assertEqual(fourth_Power_Sum(30), 14112081)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum('a')
