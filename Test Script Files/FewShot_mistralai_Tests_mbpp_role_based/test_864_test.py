import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):
    def test_palindrome_with_single_letter(self):
        self.assertIn("a", palindrome_lambda(["a", "b", "c", "aa"]))

    def test_palindrome_with_multiple_letters(self):
        self.assertIn("level", palindrome_ladder(["level", "python", "racecar", "deified"]))

    def test_empty_list(self):
        self.assertListEqual(palindrome_lambda([]), [])

    def test_single_non_palindrome(self):
        self.assertListEqual(palindrome_lambda(["abc"]), [])

    def test_all_non_palindromes(self):
        self.assertListEqual(palindrome_lambda(["abc", "def", "ghi"]), [])
