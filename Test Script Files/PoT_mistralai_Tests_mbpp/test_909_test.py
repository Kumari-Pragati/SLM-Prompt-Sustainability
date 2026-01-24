import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(previous_palindrome(101), 101)
        self.assertEqual(previous_palindrome(121), 111)
        self.assertEqual(previous_palindrome(1001), 991)
        self.assertEqual(previous_palindrome(10001), 9901)

    def test_edge_cases(self):
        self.assertEqual(previous_palindrome(0), None)
        self.assertEqual(previous_palindrome(1), None)
        self.assertEqual(previous_palindrome(11), None)

    def test_boundary_cases(self):
        self.assertEqual(previous_palindrome(2), 1)
        self.assertEqual(previous_palindrome(3), 1)
        self.assertEqual(previous_palindrome(4), 2)
        self.assertEqual(previous_palindrome(5), 3)
        self.assertEqual(previous_palindrome(6), 3)
        self.assertEqual(previous_palindrome(7), 5)
        self.assertEqual(previous_palindrome(8), 5)
        self.assertEqual(previous_palindrome(9), 6)
