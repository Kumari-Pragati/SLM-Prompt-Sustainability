import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(largest_palindrome([121, 123, 121312], 2), 121)
        self.assertEqual(largest_palindrome([121, 123, 121312], 3), -1)
        self.assertEqual(largest_palindrome([121, 123, 121312], 1), 121)

    def test_edge_cases(self):
        self.assertEqual(largest_palindrome([121], 1), 121)
        self.assertEqual(largest_palindrome([123], 1), -1)
        self.assertEqual(largest_palindrome([121, 123], 1), -1)
        self.assertEqual(largest_palindrome([121, 123], 2), 121)
        self.assertEqual(largest_palindrome([], 1), -1)
        self.assertEqual(largest_palindrome([121], 2), 121)

    def test_complex_cases(self):
        self.assertEqual(largest_palindrome([123456789, 12321, 1234567890], 2), 12321)
        self.assertEqual(largest_palindrome([123456789, 12321, 1234567890, 1232123], 3), 1232123)
        self.assertEqual(largest_palindrome([123456789, 12321, 1234567890, 1232123, 1232123456789], 4), 1232123456789)
        self.assertEqual(largest_palindrome([123456789, 12321, 1234567890, 1232123, 1232123456789, 12321234567890123], 5), 12321234567890123)
