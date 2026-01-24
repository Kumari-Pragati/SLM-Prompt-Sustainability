import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertEqual(previous_palindrome(121), 121)
        self.assertEqual(previous_palindrome(2002), 2001)
        self.assertEqual(previous_palindrome(11111), 11110)

    def test_edge_cases(self):
        self.assertEqual(previous_palindrome(0), None)
        self.assertEqual(previous_palindrome(1), None)
        self.assertEqual(previous_palindrome(999), 998)
        self.assertEqual(previous_palindrome(1000000), None)

    def test_negative_and_large_numbers(self):
        self.assertEqual(previous_palindrome(-1), None)
        self.assertEqual(previous_palindrome(10**20), None)
