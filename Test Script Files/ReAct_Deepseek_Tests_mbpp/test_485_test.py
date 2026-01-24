import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_palindrome([12321, 121, 1234321], 3), 1234321)

    def test_edge_case_single_element(self):
        self.assertEqual(largest_palindrome([121], 1), 121)

    def test_edge_case_no_palindrome(self):
        self.assertEqual(largest_palindrome([123456789], 1), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(largest_palindrome([], 0), -1)

    def test_edge_case_all_palindromes(self):
        self.assertEqual(largest_palindrome([121, 12321, 1234321], 3), 1234321)

    def test_error_case_non_integer_input(self):
        with self.assertRaises(TypeError):
            largest_palindrome(["12321", "121", "1234321"], 3)

    def test_error_case_negative_integer(self):
        with self.assertRaises(ValueError):
            largest_palindrome([-121, -12321, -1234321], 3)
