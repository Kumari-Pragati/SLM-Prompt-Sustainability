import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):
    def test_typical_anagram(self):
        texts = ["listen", "silent", "enlist", "tinsel"]
        str = "silent"
        self.assertEqual(anagram_lambda(texts, str), ["silent"])

    def test_no_anagram(self):
        texts = ["hello", "world", "python"]
        str = "silent"
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_multiple_anagrams(self):
        texts = ["listen", "silent", "enlist", "tinsel", "inlets"]
        str = "silent"
        self.assertEqual(anagram_lambda(texts, str), ["silent", "inlets"])

    def test_empty_string(self):
        texts = ["hello", "world", "python"]
        str = ""
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_empty_text(self):
        texts = []
        str = "hello"
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_invalid_input_type(self):
        texts = "hello"
        str = "hello"
        with self.assertRaises(TypeError):
            anagram_lambda(texts, str)

    def test_invalid_input_type2(self):
        texts = ["hello"]
        str = 123
        with self.assertRaises(TypeError):
            anagram_lambda(texts, str)
