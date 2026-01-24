import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_largest_palindrome_positive(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)

    def test_largest_palindrome_negative(self):
        self.assertEqual(largest_palindrome([-1, -2, -3, -4, -5, -6, -7, -8, -9], 9), -1)

    def test_largest_palindrome_zero(self):
        self.assertEqual(largest_palindrome([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 0)

    def test_largest_palindrome_empty_list(self):
        self.assertEqual(largest_palindrome([], 0), -1)

    def test_largest_palindrome_single_element(self):
        self.assertEqual(largest_palindrome([1], 1), 1)

    def test_largest_palindrome_palindrome(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 1], 10), 1)

    def test_largest_palindrome_non_palindrome(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), -1)
