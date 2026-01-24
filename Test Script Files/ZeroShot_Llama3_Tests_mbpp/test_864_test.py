import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_palindrome_lambda_empty_list(self):
        self.assertEqual(palindrome_lambda([]), [])

    def test_palindrome_lambda_single_palindrome(self):
        self.assertEqual(palindrome_lambda(['radar']), ['radar'])

    def test_palindrome_lambda_single_non_palindrome(self):
        self.assertEqual(palindrome_lambda(['hello']), [])

    def test_palindrome_lambda_multiple_palindromes(self):
        self.assertEqual(palindrome_lambda(['radar', 'hello','mom']), ['radar','mom'])

    def test_palindrome_lambda_multiple_non_palindromes(self):
        self.assertEqual(palindrome_lambda(['hello', 'world', 'abc']), [])

    def test_palindrome_lambda_mixed_palindromes_and_non_palindromes(self):
        self.assertEqual(palindrome_lambda(['radar', 'hello','mom', 'abc']), ['radar','mom'])
