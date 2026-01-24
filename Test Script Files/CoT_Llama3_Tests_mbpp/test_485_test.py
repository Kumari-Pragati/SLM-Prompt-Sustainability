import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):
    def test_largest_palindrome(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 10), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 12), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 13), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 14), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 15), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 16), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 17), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 18), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 19), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 20), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 21), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 22), 9)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24