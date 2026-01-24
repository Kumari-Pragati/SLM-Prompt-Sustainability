import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fourth_Power_Sum(0), 0)

    def test_one(self):
        self.assertEqual(fourth_Power_Sum(1), 1)

    def test_small_numbers(self):
        self.assertEqual(fourth_Power_Sum(2), 8)
        self.assertEqual(fourth_Power_Sum(3), 33)
        self.assertEqual(fourth_Power_Sum(4), 104)
        self.assertEqual(fourth_Power_Sum(5), 233)

    def test_large_numbers(self):
        self.assertEqual(fourth_Power_Sum(10), 1972)
        self.assertEqual(fourth_Power_Sum(100), 1047280)
        self.assertEqual(fourth_Power_Sum(1000), 30414772800)
