import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(words_ae("aeiou"), ["ae"])
        self.assertListEqual(words_ae("ae apple"), ["ae", "apple"])
        self.assertListEqual(words_ae("ae123"), ["ae"])

    def test_edge_case(self):
        self.assertListEqual(words_ae("a"), [])
        self.assertListEqual(words_ae("ae "), ["ae"])
        self.assertListEqual(words_ae("ae\t"), ["ae"])
        self.assertListEqual(words_ae("ae\n"), ["ae"])

    def test_corner_case(self):
        self.assertListEqual(words_ae("ae0"), ["ae"])
        self.assertListEqual(words_ae("ae_"), ["ae"])
        self.assertListEqual(words_ae("ae!"), ["ae"])
        self.assertListEqual(words_ae("ae?"), ["ae"])
        self.assertListEqual(words_ae("ae,"), ["ae"])
