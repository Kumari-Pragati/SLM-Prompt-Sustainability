import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(words_ae(""), [])

    def test_single_word(self):
        self.assertListEqual(words_ae("ae"), ["ae"])
        self.assertListEqual(words_ae("aeb"), ["aeb"])
        self.assertListEqual(words_ae("AeB"), ["AeB"])

    def test_multiple_words(self):
        self.assertListEqual(words_ae("ae word ae"), ["ae", "ae"])
        self.assertListEqual(words_ae("ae Word Ae"), ["ae", "Ae"])
        self.assertListEqual(words_ae("Ae Word Ae"), ["Ae"])

    def test_mixed_case(self):
        self.assertListEqual(words_ae("Ae WOrD aE"), ["Ae", "WOrD"])
        self.assertListEqual(words_ae("Ae 123 WOrD aE"), ["Ae", "WOrD"])
        self.assertListEqual(words_ae("Ae_123WOrD_ae"), ["Ae", "WOrD"])

    def test_multiple_ae(self):
        self.assertListEqual(words_ae("aae"), ["aae"])
        self.assertListEqual(words_ae("aae bb"), ["aae"])
        self.assertListEqual(words_ae("aae bb aae"), ["aae", "aae"])

    def test_no_match(self):
        self.assertListEqual(words_ae("abc"), [])
        self.assertListEqual(words_ae("123"), [])
        self.assertListEqual(words_ae("$%^&*"), [])
