import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_multiple_spaces(self):
        self.assertEqual(capital_words_spaces("Hello   World"), "Hello   World")

    def test_no_spaces(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "HelloWorld")

    def test_multiple_capitals(self):
        self.assertEqual(capital_words_spaces("HelloWorld123"), "Hello World 123")

    def test_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            capital_words_spaces(123)
