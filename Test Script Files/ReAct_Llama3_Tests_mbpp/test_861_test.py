import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(anagram_lambda([], "abc"), [])

    def test_single_anagram(self):
        self.assertEqual(anagram_lambda(["abc", "abc"], "abc"), ["abc"])

    def test_multiple_anagrams(self):
        self.assertEqual(anagram_lambda(["abc", "def", "abc"], "abc"), ["abc"])

    def test_no_anagrams(self):
        self.assertEqual(anagram_lambda(["abc", "def", "ghi"], "abc"), [])

    def test_empty_string(self):
        self.assertEqual(anagram_lambda(["abc", "def"], ""), [])

    def test_single_character(self):
        self.assertEqual(anagram_lambda(["a", "b", "c"], "a"), ["a"])

    def test_no_anagrams_with_duplicates(self):
        self.assertEqual(anagram_lambda(["abc", "def", "abc"], "abcabc"), [])

    def test_anagrams_with_duplicates(self):
        self.assertEqual(anagram_lambda(["abc", "abc", "def"], "abc"), ["abc"])
