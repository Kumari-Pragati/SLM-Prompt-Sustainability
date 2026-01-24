import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):
    def test_typical_case(self):
        A = [121, 12321, 123321, 1234321]
        n = len(A)
        self.assertEqual(largest_palindrome(A, n), 1234321)

    def test_edge_case(self):
        A = [121, 12321, 123321, 1234321, 0]
        n = len(A)
        self.assertEqual(largest_palindrome(A, n), 1234321)

    def test_boundary_case(self):
        A = [121, 12321, 123321, 1234321]
        n = 0
        self.assertEqual(largest_palindrome(A, n), -1)

    def test_invalid_input(self):
        A = [121, 12321, '123321', 1234321]
        n = len(A)
        with self.assertRaises(TypeError):
            largest_palindrome(A, n)
