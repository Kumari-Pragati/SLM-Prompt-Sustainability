import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertEqual(palindrome_lambda(["radar", "mom", "dad"]), ["radar", "mom", "dad"])

    def test_non_palindromes(self):
        self.assertEqual(palindrome_lambda(["hello", "world", "python"]), [])

    def test_empty_input(self):
        self.assertEqual(palindrome_lambda([]), [])

    def test_single_character(self):
        self.assertEqual(palindrome_lambda(["a", "b", "c"]), [])

    def test_empty_string(self):
        self.assertEqual(palindrome_lambda(["", "hello", "world"]), [])

    def test_palindrome_with_spaces(self):
        self.assertEqual(palindrome_lambda(["A man a plan a canal Panama", "Hello world"]), ["A man a plan a canal Panama"])

    def test_non_palindrome_with_spaces(self):
        self.assertEqual(palindrome_lambda(["Hello world", "Python is fun"]), [])
