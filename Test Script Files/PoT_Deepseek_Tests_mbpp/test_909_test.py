import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(previous_palindrome(12321), 1221)
        self.assertEqual(previous_palindrome(9876789), 98766789)
        self.assertEqual(previous_palindrome(1001), 999)

    def test_edge_cases(self):
        self.assertEqual(previous_palindrome(1000), 999)
        self.assertEqual(previous_palindrome(10000), 9999)

    def test_boundary_cases(self):
        self.assertEqual(previous_palindrome(100000), 99999)
        self.assertEqual(previous_palindrome(1000000), 999999)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            previous_palindrome("12321")
        with self.assertRaises(ValueError):
            previous_palindrome(-12321)
