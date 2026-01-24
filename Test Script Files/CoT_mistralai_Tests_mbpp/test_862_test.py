import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(n_common_words("", 5), [])

    def test_single_word(self):
        self.assertEqual(n_common_words("word", 1), [("word", 1)])

    def test_multiple_words(self):
        self.assertEqual(n_common_words("word1 word2 word1 word3", 2), [("word1", 2), ("word2", 1)])

    def test_case_insensitive(self):
        self.assertEqual(n_common_words("Word1 Word2 Word1 Word3", 2), [("word1", 2), ("word2", 1)])

    def test_n_greater_than_number_of_words(self):
        self.assertEqual(n_common_words("word1 word2", 3), [("word1", 1), ("word2", 1)])

    def test_n_equal_to_number_of_words(self):
        self.assertEqual(n_common_words("word1 word1 word2", 2), [("word1", 2)])

    def test_punctuation(self):
        self.assertEqual(n_common_words("word1, word2! word1", 2), [("word1", 2)])

    def test_numbers(self):
        self.assertEqual(n_common_words("word1 1word2", 2), [("word1", 1), ("word2", 1)])
