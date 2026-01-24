import unittest
from mbpp_864_code import palindrome_lambda
import re

class TestPalindromeLambda(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(palindrome_lambda([]), [])

    def test_single_element_list(self):
        self.assertListEqual(palindrome_lambda(["a"]), ["a"])

    def test_non_palindrome_list(self):
        self.assertListEqual(palindrome_lambda(["hello", "world"]), [])

    def test_palindrome_list(self):
        self.assertListEqual(palindrome_lambda(["racecar", "level", "madam"]), ["racecar", "level", "madam"])

    def test_mixed_list(self):
        self.assertListEqual(palindrome_lambda(["racecar", "level", "madam", "hello", "world"]), ["racecar", "level", "madam"])

    def test_special_characters(self):
        self.assertListEqual(palindrome_lambda(["A man, a plan, a canal: Panama"]), ["A man, a plan, a canal: Panama"])

    def test_case_insensitive(self):
        self.assertListEqual(palindrome_lambda(["Racecar", "Level", "Madam", "Hello", "World"]), ["Racecar", "Level", "Madam"])

    def test_multiple_spaces(self):
        self.assertListEqual(palindrome_lambda(["   racecar   ", " level   ", " madam   "]), ["racecar", "level", "madam"])

    def test_non_string_elements(self):
        self.assertListEqual(palindrome_lambda([1, 2, 3, "racecar", "level", "madam"]), ["racecar", "level", "madam"])
