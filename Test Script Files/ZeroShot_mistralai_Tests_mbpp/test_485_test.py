import unittest
from mbpp_485_code import is_palindrome, largest_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_positive(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(123454321))

    def test_is_palindrome_negative(self):
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(123456))
        self.assertFalse(is_palindrome(123456789))

class TestLargestPalindrome(unittest.TestCase):
    def test_largest_palindrome_positive(self):
        self.assertEqual(largest_palindrome([121, 12321, 123454321, 123456, 123456789], 5), 12321)
        self.assertEqual(largest_palindrome([121, 12321, 123454321, 123456, 123456789, 1234567890], 10), 123454321)

    def test_largest_palindrome_negative(self):
        self.assertEqual(largest_palindrome([121, 12321, 123454321, 123456, 123456789], 0), -1)
        self.assertEqual(largest_palindrome([121, 12321, 123454321, 123456, 123456789], 6), -1)
        self.assertEqual(largest_palindrome([], 5), -1)
        self.assertEqual(largest_palindrome([123456789], 5), -1)
