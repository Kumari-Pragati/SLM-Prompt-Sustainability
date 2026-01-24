import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 4), 181)
        self.assertEqual(largest_palindrome([45, 55, 65, 75, 87, 181, 188, 373, 380, 646, 787], 11), 787)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 101, 121, 151, 181, 373, 380, 646, 787, 808], 16), 808)

    def test_edge_cases(self):
        self.assertEqual(largest_palindrome([], 1), -1)
        self.assertEqual(largest_palindrome([1], 1), -1)
        self.assertEqual(largest_palindrome([121], 1), 121)
        self.assertEqual(largest_palindrome([121], 2), -1)
        self.assertEqual(largest_palindrome([121], 3), -1)

    def test_boundary_cases(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 19)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 20), -1)
