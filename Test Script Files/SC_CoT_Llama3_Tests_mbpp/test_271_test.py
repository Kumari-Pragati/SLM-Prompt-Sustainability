import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_even_power_sum(self):
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(2), 0)
        self.assertEqual(even_Power_Sum(3), 0)
        self.assertEqual(even_Power_Sum(4), 576)
        self.assertEqual(even_Power_Sum(5), 576)
        self.assertEqual(even_Power_Sum(6), 8640)
        self.assertEqual(even_Power_Sum(7), 8640)
        self.assertEqual(even_Power_Sum(8), 8640)
        self.assertEqual(even_Power_Sum(9), 8640)
        self.assertEqual(even_Power_Sum(10), 8640)

    def test_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(2), 0)
        self.assertEqual(even_Power_Sum(3), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
