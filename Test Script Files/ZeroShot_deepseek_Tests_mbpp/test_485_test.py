import unittest
from mbpp_485_code import largest_palindrome, is_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(12321))
        self.assertFalse(is_palindrome(12345))
        self.assertFalse(is_palindrome(123456))

    def test_largest_palindrome(self):
        self.assertEqual(largest_palindrome([121, 12321, 98765, 12345, 123456], 5), 12321)
        self.assertEqual(largest_palindrome([123, 456, 789, 321, 654], 5), -1)
        self.assertEqual(largest_palindrome([12321, 98765, 12345, 123456, 121], 5), 123456)
        self.assertEqual(largest_palindrome([121, 121, 121, 121, 121], 5), 121)
