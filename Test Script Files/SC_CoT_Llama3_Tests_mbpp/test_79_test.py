import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(word_len("hello world"))

    def test_edge_case_even_length(self):
        self.assertFalse(word_len("hello"))

    def test_edge_case_odd_length(self):
        self.assertTrue(word_len("hello world"))

    def test_edge_case_empty_string(self):
        self.assertFalse(word_len(""))

    def test_edge_case_single_word(self):
        self.assertFalse(word_len("hello"))

    def test_edge_case_multiple_words(self):
        self.assertTrue(word_len("hello world this"))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            word_len(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            word_len(None)
