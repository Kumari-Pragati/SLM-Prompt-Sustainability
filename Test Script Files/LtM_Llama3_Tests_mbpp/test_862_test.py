import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(n_common_words("", 1), [])

    def test_single_word(self):
        self.assertEqual(n_common_words("hello", 1), [('hello', 1)])

    def test_multiple_words(self):
        self.assertEqual(n_common_words("hello world hello", 2), [('hello', 2), ('world', 1)])

    def test_edge_case_n_zero(self):
        self.assertEqual(n_common_words("hello world", 0), [])

    def test_edge_case_n_max(self):
        self.assertEqual(n_common_words("hello world hello", len("hello world hello").split().unique())), [('hello', 2), ('world', 1)])

    def test_edge_case_text_empty_string(self):
        self.assertEqual(n_common_words("", 1), [])

    def test_edge_case_n_max_empty_string(self):
        self.assertEqual(n_common_words("", len("".split()).unique())), [])

    def test_edge_case_n_max_empty_string_with_n_zero(self):
        self.assertEqual(n_common_words("", 0), [])

    def test_edge_case_n_max_empty_string_with_n_max(self):
        self.assertEqual(n_common_words("", len("".split()).unique())), []

    def test_edge_case_n_max_empty_string_with_n_max_and_n_zero(self):
        self.assertEqual(n_common_words("", 0), [])
