import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_simple_case(self):
        self.assertListEqual(words_ae("ae"), ["ae"])
        self.assertListEqual(words_ae("ae word"), ["ae", "word"])
        self.assertListEqual(words_ae("word1 ae2 word3"), ["ae2"])

    def test_edge_case(self):
        self.assertListEqual(words_ae(""), [])
        self.assertListEqual(words_ae(" ae "), ["ae"])
        self.assertListEqual(words_ae("ae\t"), ["ae"])
        self.assertListEqual(words_ae("ae\n"), ["ae"])

    def test_boundary_case(self):
        self.assertListEqual(words_ae("ae\tword"), ["ae", "word"])
        self.assertListEqual(words_ae("word\tae"), ["word", "ae"])
        self.assertListEqual(words_ae("word\tae\tword"), ["word", "ae", "word"])

    def test_complex_case(self):
        self.assertListEqual(words_ae("ae1 word2 ae3"), ["ae1", "ae3"])
        self.assertListEqual(words_ae("ae1 word2 ae3 word4"), ["ae1", "ae3"])
        self.assertListEqual(words_ae("ae1 word2 ae3 word4 ae5"), ["ae1", "ae3", "ae5"])
