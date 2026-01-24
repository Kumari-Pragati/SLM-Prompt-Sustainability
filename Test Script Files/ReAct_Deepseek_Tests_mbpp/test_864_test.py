import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(palindrome_lambda(["radar", "level", "deed"]), ["radar", "level", "deed"])
        self.assertEqual(palindrome_lambda(["abcba", "12321"]), ["abcba", "12321"])

    def test_edge_cases(self):
        self.assertEqual(palindrome_lambda(["a"]), ["a"])
        self.assertEqual(palindrome_lambda(["1"]), ["1"])
        self.assertEqual(palindrome_lambda([]), [])

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            palindrome_lambda(123)
        with self.assertRaises(TypeError):
            palindrome_lambda(["abc", 123])
        with self.assertRaises(TypeError):
            palindrome_lambda(["abc", None])
