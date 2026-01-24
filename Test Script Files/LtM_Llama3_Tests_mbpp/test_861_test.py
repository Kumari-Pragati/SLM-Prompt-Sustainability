import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(anagram_lambda([], "abc"), [])

    def test_single_input(self):
        self.assertEqual(anagram_lambda(["abc"], "abc"), ["abc"])

    def test_multiple_inputs(self):
        self.assertEqual(anagram_lambda(["abc", "def", "abc"], "abc"), ["abc"])

    def test_non_anagram_input(self):
        self.assertEqual(anagram_lambda(["abc", "def"], "abc"), [])

    def test_empty_string(self):
        self.assertEqual(anagram_lambda(["abc", "def"], ""), [])

    def test_anagram_with_spaces(self):
        self.assertEqual(anagram_lambda(["abc def", "def abc"], "abc def"), ["abc def"])

    def test_anagram_with_punctuation(self):
        self.assertEqual(anagram_lambda(["hello, world!", "world, hello!"], "hello, world!"), ["hello, world!"])

    def test_anagram_with_numbers(self):
        self.assertEqual(anagram_lambda(["hello123", "123hello"], "hello123"), ["hello123"])
