import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(next_smallest_palindrome(123), 131)
        self.assertEqual(next_smallest_palindrome(12321), 12421)
        self.assertEqual(next_smallest_palindrome(999), 1001)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(next_smallest_palindrome(1000000000000000000), 1000000000001000000)
        self.assertEqual(next_smallest_palindrome(0), 1)
        self.assertEqual(next_smallest_palindrome(999999999999999999), 1000000000000000001)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(next_smallest_palindrome(12345678987654321), 12345679097654321)
        self.assertEqual(next_smallest_palindrome(123456789987654321), 1234567899987654321)
