import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(previous_palindrome(121), 111)
        self.assertEqual(previous_palindrome(101), 91)
        self.assertEqual(previous_palindrome(2002), 1991)

    def test_zero(self):
        self.assertIsNone(previous_palindrome(0))

    def test_negative_numbers(self):
        self.assertIsNone(previous_palindrome(-1))

    def test_non_palindromic_numbers(self):
        self.assertIsNone(previous_palindrome(123))
        self.assertIsNone(previous_palindrome(12345))
