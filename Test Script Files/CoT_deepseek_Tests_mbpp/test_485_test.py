import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_palindrome([121, 12321, 123321, 1234321], 4), 1234321)

    def test_single_palindrome(self):
        self.assertEqual(largest_palindrome([12344321], 1), 12344321)

    def test_no_palindrome(self):
        self.assertEqual(largest_palindrome([123456789], 1), -1)

    def test_empty_list(self):
        self.assertEqual(largest_palindrome([], 0), -1)

    def test_negative_numbers(self):
        self.assertEqual(largest_palindrome([-121, -12321, -123321, -1234321], 4), -1)

    def test_mixed_numbers(self):
        self.assertEqual(largest_palindrome([121, -12321, 123321, -1234321], 4), 123321)
