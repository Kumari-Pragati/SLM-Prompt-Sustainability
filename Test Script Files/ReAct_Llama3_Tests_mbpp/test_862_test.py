import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a typical text with some common words."
        n = 3
        expected = [('This', 1), ('is', 1), ('a', 1)]
        self.assertEqual(n_common_words(text, n), expected)

    def test_edge_case_empty_text(self):
        text = ""
        n = 3
        expected = []
        self.assertEqual(n_common_words(text, n), expected)

    def test_edge_case_single_word_text(self):
        text = "Hello"
        n = 1
        expected = [('Hello', 1)]
        self.assertEqual(n_common_words(text, n), expected)

    def test_edge_case_zero_n(self):
        text = "Hello World"
        n = 0
        expected = []
        self.assertEqual(n_common_words(text, n), expected)

    def test_edge_case_negative_n(self):
        text = "Hello World"
        n = -1
        with self.assertRaises(ValueError):
            n_common_words(text, n)

    def test_edge_case_non_integer_n(self):
        text = "Hello World"
        n = "three"
        with self.assertRaises(TypeError):
            n_common_words(text, n)

    def test_edge_case_non_string_text(self):
        text = 123
        n = 3
        with self.assertRaises(TypeError):
            n_common_words(text, n)

    def test_edge_case_non_integer_n_common_words(self):
        text = "Hello World"
        n = 3.5
        with self.assertRaises(TypeError):
            n_common_words(text, n)
