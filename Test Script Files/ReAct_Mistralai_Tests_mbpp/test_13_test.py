import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(count_common([]), [])

    def test_single_word(self):
        self.assertListEqual(count_common(["word"]), [("word", 1)])

    def test_multiple_words(self):
        self.assertListEqual(count_common(["word1", "word2", "word1", "word3", "word2"]), [("word2", 2), ("word1", 2)])

    def test_case_insensitive(self):
        self.assertListEqual(count_common(["Word1", "word2", "Word1", "word3", "Word2"]), [("word2", 2), ("Word1", 2)])

    def test_long_list(self):
        words = ["word1"] * 1000 + ["word2"] * 1000 + ["word3"] * 1000
        self.assertListEqual(count_common(words), [("word1", 1000), ("word2", 1000), ("word3", 1000)])

    def test_duplicate_top_four(self):
        words = ["word1", "word2", "word3", "word1", "word2", "word4"]
        self.assertListEqual(count_common(words), [("word1", 2), ("word2", 2), ("word3", 1), ("word4", 1)])
