import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(words_ae(""), [])

    def test_single_word(self):
        self.assertListEqual(words_ae("ae"), ["ae"])
        self.assertListEqual(words_ae("aeb"), ["aeb"])
        self.assertListEqual(words_ae("beae"), ["beae"])

    def test_multiple_words(self):
        self.assertListEqual(words_ae("ae word ae"), ["ae", "word", "ae"])
        self.assertListEqual(words_ae("ae word1 ae word2 ae"), ["ae", "word1", "ae", "word2", "ae"])
        self.assertListEqual(words_ae("ae word1 ae word2 ae word3"), ["ae", "word1", "ae", "word2", "ae", "word3"])

    def test_punctuation(self):
        self.assertListEqual(words_ae("ae, word ae."), ["ae", "word"])
        self.assertListEqual(words_ae("ae; word ae"), ["ae", "word"])
        self.assertListEqual(words_ae("ae! word ae"), ["ae", "word"])
        self.assertListEqual(words_ae("ae? word ae"), ["ae", "word"])

    def test_numbers(self):
        self.assertListEqual(words_ae("ae 123 word ae"), ["ae", "123", "word", "ae"])
        self.assertListEqual(words_ae("ae 123.45 word ae"), ["ae", "123.45", "word", "ae"])
        self.assertListEqual(words_ae("ae 123word ae"), ["ae", "123word"])

    def test_multiple_ae(self):
        self.assertListEqual(words_ae("aae bae cae"), ["aae", "bae", "cae"])
        self.assertListEqual(words_ae("aae bae cae d"), ["aae", "bae", "cae"])
