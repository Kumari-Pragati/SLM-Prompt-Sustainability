import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_edge_case_no_spaces(self):
        self.assertEqual(capital_words_spaces("HelloWorld123"), "Hello World123")

    def test_edge_case_no_uppercase(self):
        self.assertEqual(capital_words_spaces("helloworld"), "helloworld")

    def test_edge_case_no_words(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello")

    def test_edge_case_single_word_uppercase(self):
        self.assertEqual(capital_words_spaces("HELLO"), "HELLO")

    def test_edge_case_single_word_lowercase(self):
        self.assertEqual(capital_words_spaces("hello"), "hello")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(capital_words_spaces("Hello  World"), "Hello  World")

    def test_edge_case_multiple_spaces_and_uppercase(self):
        self.assertEqual(capital_words_spaces("Hello  WORLD"), "Hello  World")

    def test_edge_case_multiple_spaces_and_lowercase(self):
        self.assertEqual(capital_words_spaces("hello  world"), "hello  world")
