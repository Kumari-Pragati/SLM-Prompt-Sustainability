import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_single_word_palindrome(self):
        self.assertEqual(palindrome_lambda(["madam"]), ["madam"])

    def test_multiple_words_palindrome(self):
        self.assertEqual(palindrome_lambda(["madam", "racecar", "python"]), ["madam", "racecar"])

    def test_empty_list(self):
        self.assertEqual(palindrome_lambda([]), [])

    def test_palindrome_with_spaces(self):
        self.assertEqual(palindrome_lambda(["madam arora"]), ["madam arora"])

    def test_non_palindrome(self):
        self.assertEqual(palindrome_lambda(["python"]), [])
