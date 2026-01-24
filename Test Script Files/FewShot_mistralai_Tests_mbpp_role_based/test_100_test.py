import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(next_smallest_palindrome(121), 123)
        self.assertEqual(next_smallest_palindrome(101), 100)
        self.assertEqual(next_smallest_palindrome(9001), 9009)

    def test_zero(self):
        self.assertEqual(next_smallest_palindrome(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(next_smallest_palindrome(-1), None)
        self.assertEqual(next_smallest_palindrome(-101), None)
        self.assertEqual(next_smallest_palindrome(-9001), None)

    def test_large_numbers(self):
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize)
