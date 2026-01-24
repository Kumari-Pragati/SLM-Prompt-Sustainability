import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(palindrome_lambda(["radar", "python", "level"]), ["radar", "level"])

    def test_edge_cases(self):
        self.assertEqual(palindrome_lambda(["a"]), ["a"])
        self.assertEqual(palindrome_lambda(["12321"]), ["12321"])

    def test_corner_cases(self):
        self.assertEqual(palindrome_lambda(["123456"]), [])
        self.assertEqual(palindrome_lambda(["abcba"]), ["abcba"])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            palindrome_lambda(12345)
        with self.assertRaises(TypeError):
            palindrome_lambda(["string", 12345])
