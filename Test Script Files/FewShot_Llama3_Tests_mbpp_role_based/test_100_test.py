import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):
    def test_next_smallest_palindrome_positive(self):
        self.assertEqual(next_smallest_palindrome(123), 121)

    def test_next_smallest_palindrome_zero(self):
        self.assertEqual(next_smallest_palindrome(0), 0)

    def test_next_smallest_palindrome_negative(self):
        self.assertEqual(next_smallest_palindrome(-123), 121)

    def test_next_smallest_palindrome_edge_case(self):
        self.assertEqual(next_smallest_palindrome(12321), 12321)

    def test_next_smallest_palindrome_max_size(self):
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize)

    def test_next_smallest_palindrome_invalid_input(self):
        with self.assertRaises(TypeError):
            next_smallest_palindrome('abc')
