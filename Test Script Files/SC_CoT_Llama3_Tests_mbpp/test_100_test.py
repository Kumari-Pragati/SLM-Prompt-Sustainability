import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(next_smallest_palindrome(123), 121)
        self.assertEqual(next_smallest_palindrome(456), 454)
        self.assertEqual(next_smallest_palindrome(789), 787)

    def test_edge_cases(self):
        self.assertEqual(next_smallest_palindrome(0), 0)
        self.assertEqual(next_smallest_palindrome(1), 1)
        self.assertEqual(next_smallest_palindrome(10), 9)

    def test_boundary_cases(self):
        self.assertEqual(next_smallest_palindrome(100), 99)
        self.assertEqual(next_smallest_palindrome(1000), 999)
        self.assertEqual(next_smallest_palindrome(10000), 9999)

    def test_corner_cases(self):
        self.assertEqual(next_smallest_palindrome(11), 9)
        self.assertEqual(next_smallest_palindrome(22), 21)
        self.assertEqual(next_smallest_palindrome(33), 31)

    def test_invalid_inputs(self):
        with self.assertRaises(OverflowError):
            next_smallest_palindrome(sys.maxsize + 1)
