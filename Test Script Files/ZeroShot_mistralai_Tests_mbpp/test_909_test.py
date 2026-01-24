import unittest
from mbpp_909_code import StringIO

class TestPreviousPalindrome(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(previous_palindrome(121), 111)
        self.assertEqual(previous_palindrome(101), 91)
        self.assertEqual(previous_palindrome(2002), 1991)

    def test_zero(self):
        self.assertIsNone(previous_palindrome(0))

    def test_negative(self):
        self.assertIsNone(previous_palindrome(-1))

    def test_special_cases(self):
        self.assertEqual(previous_palindrome(11), 1)
        self.assertEqual(previous_palindrome(10), 9)
        self.assertEqual(previous_palindrome(9), 8)
        self.assertEqual(previous_palindrome(8), 7)
        self.assertEqual(previous_palindrome(7), 6)
        self.assertEqual(previous_palindrome(6), 5)
        self.assertEqual(previous_palindrome(5), 4)
        self.assertEqual(previous_palindrome(4), 3)
        self.assertEqual(previous_palindrome(3), 2)
        self.assertEqual(previous_palindrome(2), 1)
