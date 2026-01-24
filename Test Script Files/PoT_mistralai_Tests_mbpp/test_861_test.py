import unittest
from mbpp_861_code import Counter
from eighty_six_one_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_anagram_typical(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listen"), ["listen", "enlist"])
        self.assertListEqual(anagram_lambda(["abcd", "dcba"], "abcd"), ["abcd", "dcba"])
        self.assertListEqual(anagram_lambda(["cat", "dog", "mat", "act"], "act"), ["act"])

    def test_anagram_edge(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "silent"), ["silent"])
        self.assertListEqual(anagram_lambda(["abcd", "dcba"], "abcdx"), [])
        self.assertListEqual(anagram_lambda(["cat", "dog", "mat", "act"], "catx"), [])

    def test_anagram_boundary(self):
        self.assertListEqual(anagram_lambda(["", "listen"], "listen"), [])
        self.assertListEqual(anagram_lambda(["listen", ""], "listen"), ["listen"])
        self.assertListEqual(anagram_lambda(["listen", "listen"], "listen"), ["listen", "listen"])
