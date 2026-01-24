import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(previous_palindrome(1), 0)
        self.assertEqual(previous_palindrome(10), 9)
        self.assertEqual(previous_palindrome(100), 99)
        self.assertEqual(previous_palindrome(1000), 999)
        self.assertEqual(previous_palindrome(10000), 9999)

    def test_zero(self):
        self.assertIsNone(previous_palindrome(0))

    def test_negative_numbers(self):
        self.assertIsNone(previous_palindrome(-1))
        self.assertIsNone(previous_palindrome(-10))
        self.assertIsNone(previous_palindrome(-100))
        self.assertIsNone(previous_palindrome(-1000))
        self.assertIsNone(previous_palindrome(-10000))

    def test_non_integer_inputs(self):
        self.assertIsNone(previous_palindrome(1.5))
        self.assertIsNone(previous_palindrome(-2.3))
        self.assertIsNone(previous_palindrome('abc'))
        self.assertIsNone(previous_palindrome(True))
        self.assertIsNone(previous_palindrome(None))
