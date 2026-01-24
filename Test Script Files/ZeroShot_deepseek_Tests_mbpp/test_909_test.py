import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_previous_palindrome(self):
        self.assertEqual(previous_palindrome(10), 9)
        self.assertEqual(previous_palindrome(20), 11)
        self.assertEqual(previous_palindrome(100), 99)
        self.assertEqual(previous_palindrome(1000), 999)
        self.assertEqual(previous_palindrome(1234), 1221)
        self.assertEqual(previous_palindrome(12321), 1221)
        self.assertEqual(previous_palindrome(123321), 12321)
        self.assertEqual(previous_palindrome(1234554321), 12344321)
        self.assertEqual(previous_palindrome(12345654321), 12344321)
        self.assertEqual(previous_palindrome(12345677654321), 123456654321)
