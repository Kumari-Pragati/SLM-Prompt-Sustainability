import unittest
from mbpp_861_code import Counter
from861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(anagram_lambda([], ""), [])

    def test_single_item(self):
        self.assertListEqual(anagram_lambda(["hello"], "hello"), ["hello"])
        self.assertListEqual(anagram_lambda(["world"], "hello"), [])

    def test_multiple_items(self):
        self.assertListEqual(anagram_lambda(["hello", "world"], "hellow"), ["hello", "world"])
        self.assertListEqual(anagram_lambda(["hello", "world"], "hell"), [])

    def test_case_insensitive(self):
        self.assertListEqual(anagram_lambda(["hello", "world"], "olleh"), ["hello", "world"])

    def test_same_length(self):
        self.assertListEqual(anagram_lambda(["hello", "world"], "hellow"), ["hello", "world"])
        self.assertListEqual(anagram_lambda(["hello", "world"], "hello world"), [])

    def test_different_lengths(self):
        self.assertListEqual(anagram_lambda(["hello", "world"], "hell"), [])
        self.assertListEqual(anagram_lambda(["hello", "world"], "helloworld"), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, anagram_lambda, [1, 2, 3], "str")
        self.assertRaises(TypeError, anagram_lambda, ["str"], 1)
