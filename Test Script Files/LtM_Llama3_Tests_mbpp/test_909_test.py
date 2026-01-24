import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(previous_palindrome(10), 9)
        self.assertEqual(previous_palindrome(11), 10)
        self.assertEqual(previous_palindrome(12), 11)
        self.assertEqual(previous_palindrome(13), 12)
        self.assertEqual(previous_palindrome(14), 13)
        self.assertEqual(previous_palindrome(15), 14)
        self.assertEqual(previous_palindrome(16), 15)
        self.assertEqual(previous_palindrome(17), 16)
        self.assertEqual(previous_palindrome(18), 17)
        self.assertEqual(previous_palindrome(19), 18)
        self.assertEqual(previous_palindrome(20), 19)

    def test_edge(self):
        self.assertEqual(previous_palindrome(1), 1)
        self.assertEqual(previous_palindrome(2), 1)
        self.assertEqual(previous_palindrome(3), 2)
        self.assertEqual(previous_palindrome(4), 3)
        self.assertEqual(previous_palindrome(5), 4)
        self.assertEqual(previous_palindrome(6), 5)
        self.assertEqual(previous_palindrome(7), 6)
        self.assertEqual(previous_palindrome(8), 7)
        self.assertEqual(previous_palindrome(9), 8)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            previous_palindrome(None)
        with self.assertRaises(TypeError):
            previous_palindrome('a')
