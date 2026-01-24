import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(next_smallest_palindrome(1), 2)
        self.assertEqual(next_smallest_palindrome(10), 11)
        self.assertEqual(next_smallest_palindrome(20), 22)
        self.assertEqual(next_smallest_palindrome(100), 101)

    def test_edge_cases(self):
        self.assertEqual(next_smallest_palindrome(0), 1)
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize)
        self.assertEqual(next_smallest_palindrome(sys.maxsize), sys.maxsize)

    def test_palindrome_numbers(self):
        self.assertEqual(next_smallest_palindrome(121), 131)
        self.assertEqual(next_smallest_palindrome(212), 222)
        self.assertEqual(next_smallest_palindrome(343), 353)

    def test_non_palindrome_numbers(self):
        self.assertEqual(next_smallest_palindrome(123), 131)
        self.assertEqual(next_smallest_palindrome(456), 464)
        self.assertEqual(next_smallest_palindrome(789), 787)
