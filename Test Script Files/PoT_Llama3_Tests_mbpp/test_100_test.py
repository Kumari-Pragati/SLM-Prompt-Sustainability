import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(next_smallest_palindrome(123), 121)

    def test_edge_case(self):
        self.assertEqual(next_smallest_palindrome(12321), 12321)

    def test_boundary_case(self):
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize)

    def test_tricky_case(self):
        self.assertEqual(next_smallest_palindrome(123456), 121)

    def test_invalid_input(self):
        with self.assertRaises(OverflowError):
            next_smallest_palindrome(sys.maxsize)
