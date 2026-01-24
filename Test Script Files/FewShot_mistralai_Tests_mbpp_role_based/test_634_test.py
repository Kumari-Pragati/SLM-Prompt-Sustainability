import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(even_Power_Sum(4), 16)

    def test_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_negative_number(self):
        self.assertEqual(even_Power_Sum(-1), 0)

    def test_large_number(self):
        self.assertEqual(even_Power_Sum(100), 1024000)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            even_Power_Sum(3.14)
