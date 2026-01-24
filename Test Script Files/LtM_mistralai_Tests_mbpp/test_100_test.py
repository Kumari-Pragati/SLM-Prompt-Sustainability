import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertEqual(next_smallest_palindrome(1), 2)
        self.assertEqual(next_smallest_palindrome(111), 121)
        self.assertEqual(next_smallest_palindrome(12321), 123123)

    def test_edge_cases(self):
        self.assertEqual(next_smallest_palindrome(0), 1)
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize)
        self.assertEqual(next_smallest_palindrome(sys.maxsize), sys.maxsize)

    def test_complex_cases(self):
        self.assertEqual(next_smallest_palindrome(101), 1001)
        self.assertEqual(next_smallest_palindrome(10001), 100001)
        self.assertEqual(next_smallest_palindrome(1000001), 10000001)
