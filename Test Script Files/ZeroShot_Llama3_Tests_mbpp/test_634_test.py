import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_Power_Sum(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 64)
        self.assertEqual(even_Power_Sum(3), 144)
        self.assertEqual(even_Power_Sum(4), 256)
        self.assertEqual(even_Power_Sum(5), 400)
        self.assertEqual(even_Power_Sum(6), 576)
        self.assertEqual(even_Power_Sum(7), 784)
        self.assertEqual(even_Power_Sum(8), 1024)
        self.assertEqual(even_Power_Sum(9), 1296)
        self.assertEqual(even_Power_Sum(10), 1600)

    def test_even_Power_Sum_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
