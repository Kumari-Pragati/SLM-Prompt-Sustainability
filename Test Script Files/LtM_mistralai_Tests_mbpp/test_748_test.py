import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_single_word(self):
        self.assertEqual(capital_words_spaces("World"), "World")

    def test_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_all_uppercase(self):
        self.assertEqual(capital_words_spaces("HELLO WORLD"), "HELLO  WORLD")

    def test_all_lowercase(self):
        self.assertEqual(capital_words_spaces("helloworld"), "hello world")

    def test_special_characters(self):
        self.assertEqual(capital_words_spaces("Hello123World"), "Hello 123 World")

    def test_multiple_spaces(self):
        self.assertEqual(capital_words_spaces("Hello   World"), "Hello   World")

    def test_leading_trailing_spaces(self):
        self.assertEqual(capital_words_spaces("   Hello World   "), "Hello World")
