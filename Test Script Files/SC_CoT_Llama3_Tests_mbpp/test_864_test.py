import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):
    def test_palindrome_lambda_typical(self):
        self.assertEqual(palindrome_lambda(["radar", "hello", "level", "madam"]), ["radar", "level", "madam"])

    def test_palindrome_lambda_empty(self):
        self.assertEqual(palindrome_lambda([]), [])

    def test_palindrome_lambda_single_word(self):
        self.assertEqual(palindrome_lambda(["abc"]), [])

    def test_palindrome_lambda_single_palindrome(self):
        self.assertEqual(palindrome_lambda(["abcba"]), ["abcba"])

    def test_palindrome_lambda_multiple_palindromes(self):
        self.assertEqual(palindrome_lambda(["abcba", "radar", "level", "madam"]), ["abcba", "radar", "level", "madam"])

    def test_palindrome_lambda_non_string_input(self):
        with self.assertRaises(TypeError):
            palindrome_lambda([1, 2, 3])

    def test_palindrome_lambda_mixed_case(self):
        self.assertEqual(palindrome_lambda(["Radar", "Hello", "Level", "Madam"]), ["Radar", "Level", "Madam"])

    def test_palindrome_lambda_non_palindrome_with_spaces(self):
        self.assertEqual(palindrome_lambda(["hello world"]), [])

    def test_palindrome_lambda_palindrome_with_spaces(self):
        self.assertEqual(palindrome_lambda(["madam world"]), ["madam world"])
