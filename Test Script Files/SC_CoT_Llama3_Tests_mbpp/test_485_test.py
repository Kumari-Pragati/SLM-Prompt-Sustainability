import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):
    def test_largest_palindrome(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(largest_palindrome([11, 12, 13, 14, 15], 5), 11)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111], 5), 111)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 123], 5), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123], 6), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123], 7), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123], 8), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123], 9), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123], 10), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123], 11), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123], 12), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123], 13), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123, 123], 14), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123], 15), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123], 16), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123], 17), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123], 18), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123], 19), 123)
        self.assertEqual(largest_palindrome([123, 456, 789, 101, 111, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123], 20), 123)

    def test_largest_palindrome_invalid_input(self):
        with self.assertRaises(TypeError):
            largest_palindrome([], 5)
        with self.assertRaises(TypeError):
            largest_palindrome([1, 2, 3, 4, 5], 'a')
        with self.assertRaises(TypeError):
            largest_palindrome([1, 2, 3, 4, 5], -1)
        with self.assertRaises(TypeError):
            largest_palindrome([1, 2, 3, 4,