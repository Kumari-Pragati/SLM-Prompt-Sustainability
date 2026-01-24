import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(previous_palindrome(121), 121)
        self.assertEqual(previous_palindrome(111), 111)
        self.assertEqual(previous_palindrome(2002), 2001)
        self.assertEqual(previous_palindrome(1001), 999)
        self.assertEqual(previous_palindrome(10001), 9999)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(previous_palindrome(0), None)
        self.assertEqual(previous_palindrome(1), None)
        self.assertEqual(previous_palindrome(-1), None)
        self.assertEqual(previous_palindrome(9), None)
        self.assertEqual(previous_palindrome(10), None)
        self.assertEqual(previous_palindrome(100), None)
        self.assertEqual(previous_palindrome(1000), None)
        self.assertEqual(previous_palindrome(10000), None)

    def test_special_cases(self):
        self.assertEqual(previous_palindrome(2000001), 2000000)
        self.assertEqual(previous_palindrome(2000000), None)
        self.assertEqual(previous_palindrome(2000000000), None)
