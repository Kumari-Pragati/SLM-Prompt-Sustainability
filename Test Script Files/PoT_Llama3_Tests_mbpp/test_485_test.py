import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case2(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 0), -1)

    def test_edge_case3(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 6), -1)

    def test_palindrome_found(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 10), 1)

    def test_no_palindrome_found(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), -1)
