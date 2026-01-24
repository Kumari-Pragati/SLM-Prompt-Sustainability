import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello")

    def test_multiple_words(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_multiple_words_with_spaces(self):
        self.assertEqual(capital_words_spaces("Hello World"), "Hello World")

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(capital_words_spaces("Hello, World!"), "Hello, World!")

    def test_multiple_words_with_punctuation_and_spaces(self):
        self.assertEqual(capital_words_spaces("Hello, World! Foo, Bar?"), "Hello, World! Foo, Bar?")

    def test_multiple_words_with_punctuation_and_spaces_and_numbers(self):
        self.assertEqual(capital_words_spaces("Hello, World! Foo, Bar? 123"), "Hello, World! Foo, Bar? 123")

    def test_multiple_words_with_punctuation_and_spaces_and_numbers_and_special_chars(self):
        self.assertEqual(capital_words_spaces("Hello, World! Foo, Bar? 123 @#"), "Hello, World! Foo, Bar? 123 @#")
