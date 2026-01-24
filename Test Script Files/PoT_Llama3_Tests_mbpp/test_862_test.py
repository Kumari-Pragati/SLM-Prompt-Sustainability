import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(n_common_words("This is a test. This is only a test.", 2), [('this', 2), ('is', 2)])

    def test_edge_case_empty_string(self):
        self.assertEqual(n_common_words("", 2), [])

    def test_edge_case_single_word(self):
        self.assertEqual(n_common_words("Hello", 1), [('Hello', 1)])

    def test_edge_case_no_words(self):
        self.assertEqual(n_common_words("   ", 2), [])

    def test_edge_case_no_common_words(self):
        self.assertEqual(n_common_words("a b c d e", 3), [('a', 1), ('b', 1), ('c', 1)])

    def test_edge_case_n_greater_than_word_count(self):
        self.assertEqual(n_common_words("a b c d e", 6), [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)])

    def test_edge_case_n_equal_to_word_count(self):
        self.assertEqual(n_common_words("a b c d e", 5), [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)])

    def test_edge_case_n_less_than_word_count(self):
        self.assertEqual(n_common_words("a b c d e", 3), [('a', 1), ('b', 1), ('c', 1)])

    def test_edge_case_non_ascii_characters(self):
        self.assertEqual(n_common_words("a b c d é", 2), [('a', 1), ('b', 1)])

    def test_edge_case_punctuation(self):
        self.assertEqual(n_common_words("Hello, world!", 2), [('Hello', 1), ('world', 1)])
