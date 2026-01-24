import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):
    def test_typical_case(self):
        self.assertFalse(word_len("hello world"))

    def test_edge_case_even_length(self):
        self.assertFalse(word_len("abcdef"))

    def test_edge_case_odd_length(self):
        self.assertTrue(word_len("abcdefg"))

    def test_edge_case_empty_string(self):
        self.assertFalse(word_len(""))

    def test_edge_case_single_word(self):
        self.assertFalse(word_len("hello"))

    def test_edge_case_multiple_words(self):
        self.assertTrue(word_len("hello world abc"))

    def test_edge_case_single_word_even_length(self):
        self.assertFalse(word_len("abcdefg"))

    def test_edge_case_single_word_odd_length(self):
        self.assertTrue(word_len("abcdefg"))

    def test_edge_case_multiple_words_even_length(self):
        self.assertFalse(word_len("abcdef abcdef"))

    def test_edge_case_multiple_words_odd_length(self):
        self.assertTrue(word_len("abcdef abcdefg"))
