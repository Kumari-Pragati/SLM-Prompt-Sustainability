import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(previous_palindrome(12321), 12211)
        self.assertEqual(previous_palindrome(9876789), 98766789)
        self.assertEqual(previous_palindrome(10001), 9999)

    def test_edge_cases(self):
        self.assertEqual(previous_palindrome(10000), 9999)
        self.assertEqual(previous_palindrome(100000), 99999)
        self.assertEqual(previous_palindrome(123456), 123321)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            previous_palindrome('12321')
        with self.assertRaises(ValueError):
            previous_palindrome(-12321)
