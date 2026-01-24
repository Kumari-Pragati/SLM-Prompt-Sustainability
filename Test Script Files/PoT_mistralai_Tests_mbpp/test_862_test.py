import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(n_common_words("hello world hello again", 2), [("hello", 2), ("world", 1)])
        self.assertEqual(n_common_words("apple banana apple apple", 2), [("apple", 3), ("banana", 1)])

    def test_edge_case_empty_input(self):
        self.assertEqual(n_common_words("", 2), [])

    def test_edge_case_single_word(self):
        self.assertEqual(n_common_words("word", 2), [("word", 1)])

    def test_edge_case_single_word_n_1(self):
        self.assertEqual(n_common_words("word", 0), [])

    def test_edge_case_single_word_n_greater_than_count(self):
        self.assertEqual(n_common_words("word", 2), [("word", 1)])

    def test_edge_case_multiple_words_n_greater_than_count(self):
        self.assertEqual(n_common_words("apple banana", 2), [("apple", 1), ("banana", 1)])

    def test_edge_case_multiple_words_n_equal_to_count(self):
        self.assertEqual(n_common_words("apple banana", 2), [("apple", 1), ("banana", 1)])

    def test_edge_case_multiple_words_n_less_than_count(self):
        self.assertEqual(n_common_words("apple banana", 1), [("apple", 1)])

    def test_corner_case_punctuation(self):
        self.assertEqual(n_common_words("hello, world!", 2), [("hello", 1), ("world", 1)])

    def test_corner_case_numbers(self):
        self.assertEqual(n_common_words("123 apple 456 banana 789", 2), [("apple", 1), ("banana", 1)])
