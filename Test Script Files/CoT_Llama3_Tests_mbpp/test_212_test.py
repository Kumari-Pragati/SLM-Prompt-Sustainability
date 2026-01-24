import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 16)
        self.assertEqual(fourth_Power_Sum(3), 81)
        self.assertEqual(fourth_Power_Sum(4), 256)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum(-1)

    def test_zero(self):
        self.assertEqual(fourth_Power_Sum(0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum(1.5)

    def test_large_integer(self):
        self.assertEqual(fourth_Power_Sum(100), 100100100100100)
