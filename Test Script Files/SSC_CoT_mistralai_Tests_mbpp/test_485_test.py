import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 4), 181)
        self.assertEqual(largest_palindrome([45, 55, 65, 75, 87, 181, 188, 373, 383, 18456], 9), 18456)

    def test_edge_cases(self):
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 0), -1)
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 5), -1)
        self.assertEqual(largest_palindrome([], 4), -1)
        self.assertEqual(largest_palindrome([121], 1), 121)
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 50), -1)

    def test_boundary_cases(self):
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 1), 121)
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 2), 151)
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 3), 181)
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 4), 181)
        self.assertEqual(largest_palindrome([121, 151, 181, 373, 383], 5), 383)
