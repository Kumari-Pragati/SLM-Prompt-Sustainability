import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(previous_palindrome(10), 9)

    def test_edge_case_zero(self):
        with self.assertRaises(ValueError):
            previous_palindrome(0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            previous_palindrome(-1)

    def test_edge_case_one(self):
        self.assertEqual(previous_palindrome(1), None)

    def test_edge_case_palindrome(self):
        self.assertEqual(previous_palindrome(11), 11)

    def test_edge_case_non_palindrome(self):
        self.assertEqual(previous_palindrome(12), 11)
