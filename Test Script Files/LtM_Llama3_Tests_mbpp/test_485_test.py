import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):
    def test_largest_palindrome(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6], 6), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7], 7), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8], 8), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 22), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8,