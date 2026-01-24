import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(palindrome_lambda([]), [])

    def test_single_element_list(self):
        self.assertListEqual(palindrome_lambda(["a"]), ["a"])

    def test_single_word_string(self):
        self.assertListEqual(palindrome_lambda(["hello"]), ["hello"])

    def test_multiple_words_string(self):
        self.assertListEqual(palindrome_lambda(["hello", "world"]), [])

    def test_palindrome_string(self):
        self.assertListEqual(palindrome_lambda(["racecar", "level"]), ["racecar"])

    def test_mixed_case_string(self):
        self.assertListEqual(palindrome_lambda(["Racecar", "Level"]), ["Racecar"])

    def test_punctuation_string(self):
        self.assertListEqual(palindrome_lambda(["racecar.", "level!"]), ["racecar."])

    def test_numbers_string(self):
        self.assertListEqual(palindrome_lambda(["123", "321"]), [])

    def test_empty_string(self):
        self.assertListEqual(palindrome_lambda(["", "  "]), [])

    def test_whitespace_only_string(self):
        self.assertListEqual(palindrome_lambda(["   ", "  \t\n"]), [])
