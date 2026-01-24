import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 33)
        self.assertEqual(fifth_Power_Sum(3), 244)
        self.assertEqual(fifth_Power_Sum(4), 1057)
        self.assertEqual(fifth_Power_Sum(5), 3126)

    def test_zero(self):
        self.assertEqual(fifth_Power_Sum(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(fifth_Power_Sum(-1), 0)
        self.assertEqual(fifth_Power_Sum(-2), 0)

    def test_large_numbers(self):
        self.assertEqual(fifth_Power_Sum(10), 2051128)
        self.assertEqual(fifth_Power_Sum(20), 795235776)
