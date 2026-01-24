import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello")
        self.assertEqual(capital_words_spaces("world"), "world")

    def test_multiple_words(self):
        self.assertEqual(capital_words_spaces("Hello World"), "Hello World")
        self.assertEqual(capital_words_spaces("Python Programming"), "Python Programming")

    def test_mixed_case(self):
        self.assertEqual(capital_words_spaces("HeLlO wOrLd"), "HeLLO WORLD")
        self.assertEqual(capital_words_spaces("123Hello World456"), "123 Hello World 456")

    def test_punctuation(self):
        self.assertEqual(capital_words_spaces("Hello, World!"), "Hello, World!")
        self.assertEqual(capital_words_spaces("Hello@World"), "Hello @World")

    def test_numbers(self):
        self.assertEqual(capital_words_spaces("123Hello World456"), "123 Hello World 456")
        self.assertEqual(capital_words_spaces("Hello 123World"), "Hello 123 World")

    def test_long_string(self):
        long_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.assertEqual(capital_words_spaces(long_string), long_string)
