import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_palindrome([123, 121, 34543, 456654], 4), 456654)

    def test_edge_case(self):
        self.assertEqual(largest_palindrome([123, 121, 34543, 456654, 0], 5), 0)

    def test_boundary_case(self):
        self.assertEqual(largest_palindrome([123, 121, 34543, 456654, 999999], 5), 999999)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            largest_palindrome("not a list", 1)

        with self.assertRaises(ValueError):
            largest_palindrome([1, 2, 3], -1)

        with self.assertRaises(ValueError):
            largest_palindrome([1, 2, 3], 0)
