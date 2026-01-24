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
        self.assertEqual(palindrome_lambda(['hello', 'world', 'python']), [])

    def test_palindrome_lambda_mixed_palindromes_non_palindromes(self):
        self.assertEqual(palindrome_lambda(['radar', 'hello','mom', 'world']), ['radar','mom'])

    def test_palindrome_lambda_palindrome_with_spaces(self):
        self.assertEqual(palindrome_lambda(['A man, a plan, a canal, Panama']), ['A man, a plan, a canal, Panama'])

    def test_palindrome_lambda_non_palindrome_with_spaces(self):
        self.assertEqual(palindrome_lambda(['Hello, world!']), [])
