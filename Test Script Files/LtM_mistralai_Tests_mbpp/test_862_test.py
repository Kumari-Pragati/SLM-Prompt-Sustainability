import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(n_common_words("hello world hello", 2), [("hello", 2), ("world", 1)])

    def test_single_word(self):
        self.assertEqual(n_common_words("apple", 1), [("apple", 1)])

    def test_empty_input(self):
        self.assertEqual(n_common_words("", 1), [])

    def test_multiple_occurrences(self):
        self.assertEqual(n_common_words("aaa bbb ccc", 2), [("aaa", 3), ("bbb", 2)])

    def test_long_input(self):
        self.assertEqual(n_common_words("the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog".lower(), 2), [("the", 4), ("quick", 2), ("brown", 2), ("fox", 2), ("jumps", 2), ("over", 2), ("lazy", 2), ("dog", 2)])

    def test_n_greater_than_words(self):
        self.assertEqual(n_common_words("hello world hello", 3), [("hello", 2), ("world", 1), (" ", 1)])

    def test_n_less_than_words(self):
        self.assertEqual(n_common_words("hello world hello", 0), [])
