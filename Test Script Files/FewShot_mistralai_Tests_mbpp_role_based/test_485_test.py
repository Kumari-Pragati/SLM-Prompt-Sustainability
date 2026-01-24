import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(largest_palindrome([121, 123, 1213, 1212], 4), 121)
        self.assertEqual(largest_palindrome([121, 123, 1213, 1212], 1), -1)
        self.assertEqual(largest_palindrome([121, 123, 1213, 1212], 5), -1)

    def test_empty_list(self):
        self.assertEqual(largest_palindrome([], 4), -1)

    def test_single_element(self):
        self.assertEqual(largest_palindrome([121], 1), 121)
        self.assertEqual(largest_palindrome([121], 2), -1)

    def test_negative_numbers(self):
        self.assertEqual(largest_palindrome([-121, -123, -1213, -1212], 4), -121)
        self.assertEqual(largest_palindrome([-121, -123, -1213, -1212], 1), -121)
        self.assertEqual(largest_palindrome([-121, -123, -1213, -1212], 5), -1)
