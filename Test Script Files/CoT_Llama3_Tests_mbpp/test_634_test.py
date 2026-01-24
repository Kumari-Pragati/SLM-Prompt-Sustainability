import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_even_power_sum(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 80)
        self.assertEqual(even_Power_Sum(3), 256)
        self.assertEqual(even_Power_Sum(4), 576)
        self.assertEqual(even_Power_Sum(5), 1152)
        self.assertEqual(even_Power_Sum(6), 2304)
        self.assertEqual(even_Power_Sum(7), 4608)
        self.assertEqual(even_Power_Sum(8), 9216)
        self.assertEqual(even_Power_Sum(9), 18432)
        self.assertEqual(even_Power_Sum(10), 36864)

    def test_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(1), 16)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(TypeError):
            even_Power_Sum(None)
