import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(words_ae(""), [])

    def test_single_word(self):
        self.assertListEqual(words_ae("ae"), ["ae"])
        self.assertListEqual(words_ae("Ae"), [])
        self.assertListEqual(words_ae("aE"), ["aE"])

    def test_multiple_words(self):
        self.assertListEqual(words_ae("ae word ae"), ["ae", "ae"])
        self.assertListEqual(words_ae("Ae word aE"), [])
        self.assertListEqual(words_ae("aE word ae"), ["aE"])

    def test_mixed_case(self):
        self.assertListEqual(words_ae("Ae Word Ae"), [])
        self.assertListEqual(words_ae("Ae Word ae"), [])
        self.assertListEqual(words_ae("ae Word Ae"), ["ae"])
        self.assertListEqual(words_ae("ae Word ae"), ["ae", "ae"])

    def test_punctuation(self):
        self.assertListEqual(words_ae("ae, word. ae"), ["ae", "ae"])
        self.assertListEqual(words_ae("ae word. ae,"), ["ae", "ae"])
        self.assertListEqual(words_ae("ae word. ae!"), ["ae", "ae"])
        self.assertListEqual(words_ae("ae word. ae?"), ["ae", "ae"])

    def test_multiple_ae(self):
        self.assertListEqual(words_ae("aae bae cae"), ["aae", "bae", "cae"])

    def test_long_word(self):
        self.assertListEqual(words_ae("aeveryone"), ["aeveryone"])

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            words_ae(123)
        with self.assertRaises(TypeError):
            words_ae(None)
