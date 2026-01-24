import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_positive_numbers(self):
        """Test odd_Num_Sum function with positive numbers"""
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(3), 343)
        self.assertEqual(odd_Num_Sum(5), 3125)
        self.assertEqual(odd_Num_Sum(10), 10775801)

    def test_zero(self):
        """Test odd_Num_Sum function with zero"""
        self.assertEqual(odd_Num_Sum(0), 0)

    def test_negative_numbers(self):
        """Test odd_Num_Sum function with negative numbers"""
        self.assertEqual(odd_Num_Sum(-1), -1)
        self.assertRaises(ValueError, odd_Num_Sum, -2)  # Check for ValueError when n < 1

    def test_large_numbers(self):
        """Test odd_Num_Sum function with large numbers"""
        self.assertEqual(odd_Num_Sum(1000001), 13743869132892300241)
        self.assertRaises(OverflowError, odd_Num_Sum, 1000000000000000001)  # Check for OverflowError when n exceeds the maximum integer value
