import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(previous_palindrome(12321), 1221)

    def test_single_digit_palindrome(self):
        self.assertEqual(previous_palindrome(1), 0)

    def test_large_palindrome(self):
        self.assertEqual(previous_palindrome(9090909), 9080809)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            previous_palindrome(-12321)

    def test_zero(self):
        with self.assertRaises(ValueError):
            previous_palindrome(0)

    def test_large_number(self):
        self.assertEqual(previous_palindrome(10**10), 9999999999)
