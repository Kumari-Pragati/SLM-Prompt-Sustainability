import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(even_Power_Sum(4), 16)
        self.assertEqual(even_Power_Sum(16), 4096)
        self.assertEqual(even_Power_Sum(25), 16796)

    def test_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(even_Power_Sum(-1), 0)
        self.assertEqual(even_Power_Sum(-4), 0)
        self.assertEqual(even_Power_Sum(-25), 0)

    def test_large_numbers(self):
        self.assertEqual(even_Power_Sum(100), 104857600)
        self.assertEqual(even_Power_Sum(1000), 1073741824000)
        self.assertEqual(even_Power_Sum(10000), 109951162777600000)
