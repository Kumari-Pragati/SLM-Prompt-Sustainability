import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(extract_string("", 3), [])

    def test_single_word(self):
        self.assertListEqual(extract_string("word", 3), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(extract_string("word1 word2 word3", 3), ["word1", "word2", "word3"])

    def test_single_word_longer_than_l(self):
        self.assertListEqual(extract_string("word", 2), [])

    def test_multiple_words_shorter_than_l(self):
        self.assertListEqual(extract_string("w", 3), [])

    def test_punctuation(self):
        self.assertListEqual(extract_string("word,word2 word3!", 3), ["word", "word2", "word3"])

    def test_mixed_case(self):
        self.assertListEqual(extract_string("Word1 Word2 Word3", 3), ["Word1", "Word2", "Word3"])

    def test_multiple_spaces(self):
        self.assertListEqual(extract_string(" word1 word2 word3 ", 3), ["word1", "word2", "word3"])
