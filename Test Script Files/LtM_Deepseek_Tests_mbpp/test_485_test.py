import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(largest_palindrome([121, 12321, 123321], 3), 123321)
        self.assertEqual(largest_palindrome([123, 321, 121], 3), 121)

    def test_edge_conditions(self):
        self.assertEqual(largest_palindrome([], 0), -1)
        self.assertEqual(largest_palindrome([123, 321, 121], 0), -1)
        self.assertEqual(largest_palindrome([123, 321, 121], -1), -1)

    def test_boundary_conditions(self):
        self.assertEqual(largest_palindrome([121, 121, 121], 3), 121)
        self.assertEqual(largest_palindrome([12321, 12321, 12321], 3), 12321)

    def test_complex_cases(self):
        self.assertEqual(largest_palindrome([123454321, 1234554321, 12345654321], 3), 12345654321)
        self.assertEqual(largest_palindrome([123456789, 987654321, 123456789], 3), 987654321)
