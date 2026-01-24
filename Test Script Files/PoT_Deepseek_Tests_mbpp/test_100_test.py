import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(next_smallest_palindrome(123), 131)
        self.assertEqual(next_smallest_palindrome(12321), 12421)
        self.assertEqual(next_smallest_palindrome(999), 1001)

    def test_edge_cases(self):
        self.assertEqual(next_smallest_palindrome(1000), 1001)
        self.assertEqual(next_smallest_palindrome(9999), 10001)

    def test_corner_cases(self):
        self.assertEqual(next_smallest_palindrome(123456789), 123456797654321)
        self.assertEqual(next_smallest_palindrome(987654321), 1000000001)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            next_smallest_palindrome("123")
        with self.assertRaises(ValueError):
            next_smallest_palindrome(-1)
