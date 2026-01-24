import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_typical_input(self):
        text = "This is a test sentence. It has multiple words."
        n = 3
        expected_output = [('This', 1), ('is', 1), ('a', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_zero_n(self):
        text = "This is a test sentence. It has multiple words."
        n = 0
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_empty_text(self):
        text = ""
        n = 3
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_single_word_text(self):
        text = "Hello"
        n = 3
        expected_output = [('Hello', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_single_word_text_zero_n(self):
        text = "Hello"
        n = 0
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_non_numeric_n(self):
        text = "This is a test sentence. It has multiple words."
        n = 'three'
        with self.assertRaises(TypeError):
            n_common_words(text, n)

    def test_edge_case_negative_n(self):
        text = "This is a test sentence. It has multiple words."
        n = -3
        with self.assertRaises(TypeError):
            n_common_words(text, n)

    def test_edge_case_non_string_text(self):
        text = [1, 2, 3]
        n = 3
        with self.assertRaises(TypeError):
            n_common_words(text, n)

    def test_edge_case_non_integer_n(self):
        text = "This is a test sentence. It has multiple words."
        n = 3.5
        with self.assertRaises(TypeError):
            n_common_words(text, n)
