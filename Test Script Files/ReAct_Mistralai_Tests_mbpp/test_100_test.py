import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_positive_numbers(self):
        """Test next_smallest_palindrome with positive numbers"""
        self.assertEqual(next_smallest_palindrome(1), 2)
        self.assertEqual(next_smallest_palindrome(10), 11)
        self.assertEqual(next_smallest_palindrome(100), 101)
        self.assertEqual(next_smallest_palindrome(1000), 1001)
        self.assertEqual(next_smallest_palindrome(10000), 10001)

    def test_zero(self):
        """Test next_smallest_palindrome with zero"""
        self.assertEqual(next_smallest_palindrome(0), 1)

    def test_negative_numbers(self):
        """Test next_smallest_palindrome with negative numbers"""
        self.assertEqual(next_smallest_palindrome(-1), -2)
        self.assertEqual(next_smallest_palindrome(-10), -11)
        self.assertEqual(next_smallest_palindrome(-100), -101)
        self.assertEqual(next_smallest_palindrome(-1000), -1001)
        self.assertEqual(next_smallest_palindrome(-10000), -9999)

    def test_max_int(self):
        """Test next_smallest_palindrome with sys.maxsize"""
        self.assertEqual(next_smallest_palindrome(sys.maxsize), sys.maxsize + 1)

    def test_palindrome(self):
        """Test next_smallest_palindrome with palindrome numbers"""
        self.assertEqual(next_smallest_palindrome(111), 113)
        self.assertEqual(next_smallest_palindrome(12321), 12323)
        self.assertEqual(next_smallest_palindrome(1234321), 1234323)
