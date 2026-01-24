import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_positive_numbers(self):
        """Test positive numbers as input"""
        self.assertEqual(previous_palindrome(121), 121)
        self.assertEqual(previous_palindrome(2002), 2000)
        self.assertEqual(previous_palindrome(909), 909)
        self.assertEqual(previous_palindrome(1001), 1001)
        self.assertEqual(previous_palindrome(9999), 999)

    def test_zero(self):
        """Test zero as input"""
        self.assertIsNone(previous_palindrome(0))

    def test_negative_numbers(self):
        """Test negative numbers as input"""
        self.assertIsNone(previous_palindrome(-1))
        self.assertIsNone(previous_palindrome(-100))
        self.assertIsNone(previous_palindrome(-909))

    def test_non_palindromes(self):
        """Test non-palindromes as input"""
        self.assertIsNone(previous_palindrome(123))
        self.assertIsNone(previous_palindrome(2021))
        self.assertIsNone(previous_palindrome(998))
