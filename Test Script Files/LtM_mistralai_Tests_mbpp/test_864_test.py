import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertListEqual(palindrome_lambda(["racecar", "level"]), ["racecar"])

    def test_empty_list(self):
        self.assertListEqual(palindrome_lambda([]), [])

    def test_single_word(self):
        self.assertListEqual(palindrome_lambda(["hello"]), [])

    def test_non_palindrome(self):
        self.assertListEqual(palindrome_lambda(["python", "javascript"]), [])

    def test_mixed_palindrome_non_palindrome(self):
        self.assertListEqual(palindrome_lambda(["python", "level", "racecar", "javascript"]), ["level", "racecar"])

    def test_palindrome_with_special_characters(self):
        self.assertListEqual(palindrome_lambda(["A man, a plan, a canal: Panama"]), ["A man, a plan, a canal: Panama"])

    def test_palindrome_with_numbers(self):
        self.assertListEqual(palindrome_lambda(["123abc321", "radar"]), ["radar"])
