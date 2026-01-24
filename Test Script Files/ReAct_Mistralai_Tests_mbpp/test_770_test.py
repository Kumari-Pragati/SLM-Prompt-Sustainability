import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_positive_integer(self):
        """Test odd_Num_Sum function with positive integer"""
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(3), 81)
        self.assertEqual(odd_Num_Sum(5), 1533)
        self.assertEqual(odd_Num_Sum(100), 1431601)

    def test_zero(self):
        """Test odd_Num_Sum function with zero"""
        self.assertEqual(odd_Num_Sum(0), 0)

    def test_negative_integer(self):
        """Test odd_Num_Sum function with negative integer"""
        self.assertEqual(odd_Num_Sum(-1), -1)
        self.assertRaises(ValueError, odd_Num_Sum, -2)

    def test_large_integer(self):
        """Test odd_Num_Sum function with large integer"""
        self.assertRaises(OverflowError, odd_Num_Sum, 2**31)
