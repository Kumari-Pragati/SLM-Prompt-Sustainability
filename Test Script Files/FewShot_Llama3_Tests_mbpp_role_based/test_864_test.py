import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):
    def test_palindrome_string(self):
        self.assertEqual(palindrome_lambda(["radar", "hello", "madam"]), ["radar", "madam"])

    def test_non_palindrome_string(self):
        self.assertEqual(palindrome_lambda(["hello", "world", "python"]), [])

    def test_empty_list(self):
        self.assertEqual(palindrome_lambda([]), [])

    def test_single_palindrome_string(self):
        self.assertEqual(palindrome_lambda(["abcba"]), ["abcba"])

    def test_single_non_palindrome_string(self):
        self.assertEqual(palindrome_lambda(["hello"]), [])

    def test_multiple_palindrome_strings(self):
        self.assertEqual(palindrome_lambda(["radar", "madam", "abcba"]), ["radar", "madam", "abcba"])

    def test_multiple_non_palindrome_strings(self):
        self.assertEqual(palindrome_lambda(["hello", "world", "python", "java"]), [])
