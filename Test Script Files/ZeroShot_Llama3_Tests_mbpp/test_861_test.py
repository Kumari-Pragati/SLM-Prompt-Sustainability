import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_anagram_lambda(self):
        texts = ["cat", "dog", "act", "tac", "god"]
        str = "act"
        self.assertEqual(anagram_lambda(texts, str), ["act", "tac"])
        
        texts = ["hello", "world", "olleh", "dlrow"]
        str = "hello"
        self.assertEqual(anagram_lambda(texts, str), ["hello", "olleh"])
        
        texts = ["abc", "def", "ghi", "jkl"]
        str = "abc"
        self.assertEqual(anagram_lambda(texts, str), ["abc"])
        
        texts = ["abc", "def", "ghi", "jkl", "abc"]
        str = "abc"
        self.assertEqual(anagram_lambda(texts, str), ["abc", "abc"])
        
        texts = ["abc", "def", "ghi", "jkl", "mno"]
        str = "abc"
        self.assertEqual(anagram_lambda(texts, str), ["abc"])
        
        texts = []
        str = "abc"
        self.assertEqual(anagram_lambda(texts, str), [])
