import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):
    def test_fifth_power_sum(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 32)
        self.assertEqual(fifth_Power_Sum(3), 144)
        self.assertEqual(fifth_Power_Sum(4), 544)
        self.assertEqual(fifth_Power_Sum(5), 1235)
        self.assertEqual(fifth_Power_Sum(10), 161700)

    def test_fifth_power_sum_edge_cases(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(1), 1)

    def test_fifth_power_sum_invalid_inputs(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum('a')
        with self.assertRaises(TypeError):
            fifth_Power_Sum(None)
        with self.assertRaises(TypeError):
            fifth_Power_Sum(1.5)
