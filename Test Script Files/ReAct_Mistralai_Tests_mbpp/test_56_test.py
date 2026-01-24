import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_positive_numbers(self):
        """Test check function with positive numbers"""
        self.assertTrue(check(123))
        self.assertTrue(check(987))
        self.assertTrue(check(555))

    def test_zero(self):
        """Test check function with zero"""
        self.assertFalse(check(0))

    def test_negative_numbers(self):
        """Test check function with negative numbers"""
        self.assertFalse(check(-123))
        self.assertFalse(check(-987))
        self.assertFalse(check(-555))

    def test_large_numbers(self):
        """Test check function with large numbers"""
        self.assertTrue(check(123456789))
        self.assertTrue(check(987654321))

    def test_single_digit_numbers(self):
        """Test check function with single digit numbers"""
        for num in range(10):
            self.assertFalse(check(num))

    def test_edge_cases(self):
        """Test check function with edge cases"""
        self.assertFalse(check(1024))  # Largest 32-bit integer
        self.assertTrue(check(1023))  # One less than the largest 32-bit integer
