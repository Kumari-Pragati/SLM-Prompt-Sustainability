import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_power_sum(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 64)
        self.assertEqual(even_Power_Sum(3), 144)
        self.assertEqual(even_Power_Sum(4), 256)
        self.assertEqual(even_Power_Sum(5), 400)

    def test_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 64)
        self.assertEqual(even_Power_Sum(3), 144)
        self.assertEqual(even_Power_Sum(4), 256)
        self.assertEqual(even_Power_Sum(5), 400)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            even_Power_Sum(-1)
