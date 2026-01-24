import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(next_smallest_palindrome(123), 131)

    def test_edge_case(self):
        self.assertEqual(next_smallest_palindrome(999), 1001)

    def test_boundary_case(self):
        self.assertEqual(next_smallest_palindrome(1000), 1001)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            next_smallest_palindrome("123")
