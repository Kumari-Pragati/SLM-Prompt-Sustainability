import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(palindrome_lambda([]), [])

    def test_single_palindrome(self):
        self.assertEqual(palindrome_lambda(['radar']), ['radar'])

    def test_multiple_palindromes(self):
        self.assertEqual(palindrome_lambda(['radar', 'hello', 'level']), ['radar', 'level'])

    def test_non_palindromes(self):
        self.assertEqual(palindrome_lambda(['hello', 'world', 'abc']), [])

    def test_mixed_palindromes_and_non_palindromes(self):
        self.assertEqual(palindrome_lambda(['radar', 'hello', 'level', 'abc']), ['radar', 'level'])

    def test_empty_string(self):
        self.assertEqual(palindrome_lambda(['']), [])

    def test_single_palindrome_string(self):
        self.assertEqual(palindrome_lambda(['radar']), ['radar'])

    def test_multiple_palindrome_strings(self):
        self.assertEqual(palindrome_lambda(['radar', 'hello', 'level']), ['radar', 'level'])

    def test_non_palindrome_strings(self):
        self.assertEqual(palindrome_lambda(['hello', 'world', 'abc']), [])

    def test_mixed_palindrome_and_non_palindrome_strings(self):
        self.assertEqual(palindrome_lambda(['radar', 'hello', 'level', 'abc']), ['radar', 'level'])
