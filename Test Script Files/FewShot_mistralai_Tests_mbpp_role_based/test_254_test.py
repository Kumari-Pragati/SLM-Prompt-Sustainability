import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertListEqual(words_ae("The cat ate the cake"), ["cat", "cake"])

    def test_edge_case_single_word(self):
        self.assertListEqual(words_ae("ae"), ["ae"])

    def test_edge_case_no_matches(self):
        self.assertListEqual(words_ae("abcdefg"), [])

    def test_edge_case_multiple_matches(self):
        self.assertListEqual(words_ae("aeio"), ["ae", "io"])

    def test_edge_case_leading_and_trailing_spaces(self):
        self.assertListEqual(words_ae(" ae ae b "), ["ae"])

    def test_edge_case_punctuation(self):
        self.assertListEqual(words_ae("The cat ate, the cake!"), ["cat", "cake"])
