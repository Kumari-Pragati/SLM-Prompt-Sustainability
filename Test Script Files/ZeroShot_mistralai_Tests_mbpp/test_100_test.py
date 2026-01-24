import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_next_smallest_palindrome(self):
        self.assertEqual(next_smallest_palindrome(123), 121)
        self.assertEqual(next_smallest_palindrome(121), 123)
        self.assertEqual(next_smallest_palindrome(101), 1001)
        self.assertEqual(next_smallest_palindrome(1001), 10001)
        self.assertEqual(next_smallest_palindrome(10001), 100001)
        self.assertEqual(next_smallest_palindrome(100001), 1000001)
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize - 111)
        self.assertEqual(next_smallest_palindrome(sys.maxsize), sys.maxsize - 1)
