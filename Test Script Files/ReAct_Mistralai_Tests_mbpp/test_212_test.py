import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_positive_integer(self):
        """Test fourth_Power_Sum with positive integers"""
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 8)
        self.assertEqual(fourth_Power_Sum(3), 513)
        self.assertEqual(fourth_Power_Sum(10), 197281)

    def test_zero(self):
        """Test fourth_Power_Sum with zero"""
        self.assertEqual(fourth_Power_Sum(0), 0)

    def test_negative_integer(self):
        """Test fourth_Power_Sum with negative integers"""
        self.assertEqual(fourth_Power_Sum(-1), math.isnan(fourth_Power_Sum(-1)))
        self.assertEqual(fourth_Power_Sum(-2), math.isnan(fourth_Power_Sum(-2)))

    def test_large_integer(self):
        """Test fourth_Power_Sum with large integers"""
        self.assertEqual(fourth_Power_Sum(math.pow(2, 31) - 1), math.pow(2, 120) - 1)
        self.assertEqual(fourth_Power_Sum(math.pow(2, 31)), math.pow(2, 121))

    def test_float(self):
        """Test fourth_Power_Sum with float values"""
        self.assertAlmostEqual(fourth_Power_Sum(2.5), math.pow(2.5, 4))
