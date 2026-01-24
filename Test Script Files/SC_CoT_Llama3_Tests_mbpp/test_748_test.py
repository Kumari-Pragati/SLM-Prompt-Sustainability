import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(capital_words_spaces("Hello World"), "Hello World")

    def test_edge_case_uppercase(self):
        self.assertEqual(capital_words_spaces("HELLO WORLD"), "HELLO World")

    def test_edge_case_lowercase(self):
        self.assertEqual(capital_words_spaces("hello world"), "hello world")

    def test_edge_case_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello")

    def test_edge_case_single_space(self):
        self.assertEqual(capital_words_spaces(" "), " ")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(capital_words_spaces("   "), "   ")

    def test_edge_case_multiple_spaces_with_words(self):
        self.assertEqual(capital_words_spaces("Hello   World"), "Hello   World")

    def test_edge_case_punctuation(self):
        self.assertEqual(capital_words_spaces("Hello, World!"), "Hello, World!")

    def test_edge_case_non_ascii_characters(self):
        self.assertEqual(capital_words_spaces("Hello, World!"), "Hello, World!")

    def test_edge_case_multiple_sentences(self):
        self.assertEqual(capital_words_spaces("Hello, World! This is a test."), "Hello, World! This is a test.")

    def test_edge_case_multiple_sentences_with_punctuation(self):
        self.assertEqual(capital_words_spaces("Hello, World! This is a test. And another one."), "Hello, World! This is a test. And another one.")

    def test_edge_case_multiple_sentences_with_punctuation_and_non_ascii_characters(self):
        self.assertEqual(capital_words_spaces("Hello, World! This is a test. And another one. ¡Hola!"), "Hello, World! This is a test. And another one. ¡Hola!")
