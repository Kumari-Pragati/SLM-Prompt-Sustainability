import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):
    def test_anagram_found(self):
        texts = ["listen", "silent", "enlist", "tinsel"]
        str = "silent"
        self.assertEqual(anagram_lambda(texts, str), ["silent"])

    def test_anagram_not_found(self):
        texts = ["hello", "world", "python"]
        str = "silent"
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_empty_string(self):
        texts = ["hello", "world", "python"]
        str = ""
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_empty_text_list(self):
        texts = []
        str = "hello"
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_single_text(self):
        texts = ["hello"]
        str = "hello"
        self.assertEqual(anagram_lambda(texts, str), ["hello"])
