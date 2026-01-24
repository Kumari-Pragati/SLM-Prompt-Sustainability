import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(next_smallest_palindrome(121), 123)
        self.assertEqual(next_smallest_palindrome(2002), 2001)
        self.assertEqual(next_smallest_palindrome(10001), 9999)
        self.assertEqual(next_smallest_palindrome(100000), 99999)
        self.assertEqual(next_smallest_palindrome(sys.maxsize // 10), sys.maxsize // 11)

    def test_edge_cases(self):
        self.assertEqual(next_smallest_palindrome(0), 1)
        self.assertEqual(next_smallest_palindrome(1), 2)
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize - 2)
        self.assertEqual(next_smallest_palindrome(sys.maxsize), sys.maxsize - 1)

    def test_boundary_cases(self):
        self.assertEqual(next_smallest_palindrome(1111), 1113)
        self.assertEqual(next_smallest_palindrome(20001), 20003)
        self.assertEqual(next_smallest_palindrome(999999), 999997)
