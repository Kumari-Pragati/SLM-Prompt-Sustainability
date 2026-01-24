import unittest
from485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(largest_palindrome([121, 123, 1213, 12012, 121], 5), 121)
        self.assertEqual(largest_palindrome([121, 123, 1213, 12012, 121], 1), -1)
        self.assertEqual(largest_palindrome([121, 123, 1213, 12012, 121], 6), -1)

    def test_edge_case_single_digit(self):
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(largest_palindrome([1, 2, 3, 4, 5], 2), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(largest_palindrome([], 1), -1)

    def test_edge_case_single_palindrome(self):
        self.assertEqual(largest_palindrome([121], 1), 121)
        self.assertEqual(largest_palindrome([121], 2), -1)

    def test_edge_case_all_palindromes(self):
        self.assertEqual(largest_palindrome([121, 123, 1213, 12012, 121], 5), 121)

    def test_edge_case_no_palindromes(self):
        self.assertEqual(largest_palindrome([123, 1213, 12012, 121], 5), -1)
