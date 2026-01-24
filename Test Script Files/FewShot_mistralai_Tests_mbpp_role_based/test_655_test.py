import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 256)
        self.assertEqual(fifth_Power_Sum(3), 19683)
        self.assertEqual(fifth_Power_Sum(10), 327680)

    def test_zero(self):
        self.assertEqual(fifth_Power_Sum(0), 0)

    def test_negative_integer(self):
        self.assertEqual(fifth_Power_Sum(-1), -1)
        self.assertEqual(fifth_Power_Sum(-2), -32768)
        self.assertEqual(fifth_Power_Sum(-3), -19683)
