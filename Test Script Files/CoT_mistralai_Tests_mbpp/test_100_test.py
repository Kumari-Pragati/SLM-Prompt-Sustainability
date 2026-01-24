import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(next_smallest_palindrome(1), 2)
        self.assertEqual(next_smallest_palindrome(101), 103)
        self.assertEqual(next_smallest_palindrome(1001), 1003)
        self.assertEqual(next_smallest_palindrome(10001), 10003)
        self.assertEqual(next_smallest_palindrome(100001), 100003)

    def test_large_numbers(self):
        self.assertEqual(next_smallest_palindrome(sys.maxsize // 10), sys.maxsize // 10 * 10)
        self.assertEqual(next_smallest_palindrome(sys.maxsize // 100), sys.maxsize // 100 * 100)
        self.assertEqual(next_smallest_palindrome(sys.maxsize // 1000), sys.maxsize // 1000 * 1000)

    def test_edge_cases(self):
        self.assertEqual(next_smallest_palindrome(0), 1)
        self.assertEqual(next_smallest_palindrome(11), 11)
        self.assertEqual(next_smallest_palindrome(100), 101)
        self.assertEqual(next_smallest_palindrome(10101), 10103)
        self.assertEqual(next_smallest_palindrome(1000001), 1000003)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, next_smallest_palindrome, 'abc')
        self.assertRaises(TypeError, next_smallest_palindrome, -1)
        self.assertRaises(TypeError, next_smallest_palindrome, 0.5)
