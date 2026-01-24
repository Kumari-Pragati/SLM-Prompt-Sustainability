import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_positive_numbers(self):
        """Test positive numbers that are a sum of powers of two"""
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(10))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(24))

    def test_zero(self):
        """Test zero"""
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-1))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-2))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-3))

    def test_one(self):
        """Test the case of 1"""
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))

    def test_edge_cases(self):
        """Test edge cases"""
        self.assertTrue(is_Sum_Of_Powers_Of_Two(3))  # 2^1 + 2^0
        self.assertTrue(is_Sum_Of_Powers_Of_Two(5))  # 2^2 + 2^0
        self.assertFalse(is_Sum_Of_Powers_Of_Two(6))  # Not a sum of powers of 2
        self.assertTrue(is_Sum_Of_Powers_Of_Two(7))  # 2^3 + 2^0
        self.assertFalse(is_Sum_Of_Powers_Of_Two(8))  # Not a sum of powers of 2
        self.assertTrue(is_Sum_Of_Powers_Of_Two(9))  # 2^3 + 2^1
        self.assertFalse(is_Sum_Of_Powers_Of_Two(10))  # Not a sum of powers of 2
