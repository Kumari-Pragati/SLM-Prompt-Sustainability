import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_Power_Sum(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 14916)
        self.assertEqual(even_Power_Sum(3), 234256)
        self.assertEqual(even_Power_Sum(4), 3521616)
        self.assertEqual(even_Power_Sum(5), 50801560)
