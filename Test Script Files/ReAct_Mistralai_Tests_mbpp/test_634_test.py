import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_positive_integer(self):
        """Test even power sum for positive integers"""
        self.assertEqual(even_Power_Sum(1), 8)
        self.assertEqual(even_Power_Sum(2), 80)
        self.assertEqual(even_Power_Sum(3), 288)
        self.assertEqual(even_Power_Sum(4), 640)
        self.assertEqual(even_Power_Sum(5), 1344)

    def test_zero(self):
        """Test even power sum for zero"""
        self.assertEqual(even_Power_Sum(0), 0)

    def test_negative_integer(self):
        """Test even power sum for negative integers"""
        self.assertEqual(even_Power_Sum(-1), TypeError)

    def test_large_integer(self):
        """Test even power sum for large integers"""
        self.assertEqual(even_Power_Sum(1000), TypeError)
