import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_empty_text(self):
        self.assertEqual(n_common_words("", 5), [])

    def test_single_word(self):
        self.assertEqual(n_common_words("word", 1), [("word", 1)])

    def test_multiple_words(self):
        self.assertEqual(n_common_words("word1 word2 word1 word3", 2), [("word1", 2), ("word2", 1)])

    def test_multiple_words_with_duplicates(self):
        self.assertEqual(n_common_words("word1 word1 word2 word1", 2), [("word1", 3), ("word2", 1)])

    def test_long_text(self):
        long_text = " ".join([f"word_{i}" for i in range(1, 101)])
        self.assertEqual(n_common_words(long_text, 10), [("word_10", 1), ("word_20", 1), ("word_30", 1), ("word_40", 1), ("word_50", 1), ("word_60", 1), ("word_70", 1), ("word_80", 1), ("word_90", 1), ("word_100", 1)])

    def test_non_alphabetic_characters(self):
        self.assertEqual(n_common_words("word1#$%^&*()_", 2), [("word1", 1)])

    def test_n_greater_than_word_count(self):
        self.assertEqual(n_common_words("word", 100), [])

    def test_n_less_than_zero(self):
        self.assertEqual(n_common_words("word", -1), [])
