import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_largest_palindrome(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), 99)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), 909)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)

    def test_is_palindrome(self):
        self.assertTrue(largest_palindrome.is_palindrome(121))
        self.assertFalse(largest_palindrome.is_palindrome(123))
        self.assertTrue(largest_palindrome.is_palindrome(12321))
        self.assertFalse(largest_palindrome.is_palindrome(123456))
        self.assertTrue(largest_palindrome.is_palindrome(1))
        self.assertTrue(largest_palindrome.is_palindrome(10))
        self.assertFalse(largest_palindrome.is_palindrome(123))
