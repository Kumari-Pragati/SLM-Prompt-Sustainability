import unittest
from mbpp_861_code import Counter
from copy import deepcopy
from 861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_anagram_typical(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listen"), ["listen", "enlist"])
        self.assertListEqual(anagram_lambda(["cat", "dog", "act", "god"], "act"), ["act", "god"])

    def test_anagram_edge_cases(self):
        self.assertListEqual(anagram_lambda(["cat", "dog", "act", "god"], ""), [])
        self.assertListEqual(anagram_lambda(["cat", "dog", "act", "god"], "a"), [])
        self.assertListEqual(anagram_lambda(["cat", "dog", "act", "god"], "aa"), [])

    def test_anagram_invalid_input(self):
        self.assertRaises(TypeError, anagram_lambda, ["cat", "dog", "act", "god"], 1)
        self.assertRaises(TypeError, anagram_lambda, ["cat", "dog", "act", "god"], [1, 2, 3])

    def test_anagram_performance(self):
        long_texts = [deepcopy(str(i)) for i in range(10000)]
        self.assertNotEqual(len(anagram_lambda(long_texts, "".join(long_texts[0:10]))), len(long_texts))
