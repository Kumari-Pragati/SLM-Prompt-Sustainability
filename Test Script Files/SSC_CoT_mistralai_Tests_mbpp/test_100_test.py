import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(next_smallest_palindrome(121), 123)
        self.assertEqual(next_smallest_palindrome(2002), 2003)
        self.assertEqual(next_smallest_palindrome(9009), 9011)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(next_smallest_palindrome(0), 1)
        self.assertEqual(next_smallest_palindrome(1), 2)
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize)
        self.assertEqual(next_smallest_palindrome(sys.maxsize), sys.maxsize)

    def test_palindromes(self):
        self.assertEqual(next_smallest_palindrome(11), 121)
        self.assertEqual(next_smallest_palindrome(101), 111)
        self.assertEqual(next_smallest_palindrome(12321), 12323)
        self.assertEqual(next_smallest_palindrome(123454321), 123454323)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, next_smallest_palindrome, 'abc')
        self.assertRaises(TypeError, next_smallest_palindrome, -1)
        self.assertRaises(TypeError, next_smallest_palindrome, 3.14)
