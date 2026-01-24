import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(previous_palindrome(10), 9)

    def test_edge_case_start(self):
        self.assertEqual(previous_palindrome(1), None)

    def test_edge_case_end(self):
        self.assertEqual(previous_palindrome(100), 99)

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            previous_palindrome(0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            previous_palindrome(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            previous_palindrome('a')

    def test_edge_case_non_positive(self):
        with self.assertRaises(TypeError):
            previous_palindrome(-10)
