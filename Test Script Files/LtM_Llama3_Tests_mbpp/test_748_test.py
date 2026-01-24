import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(capital_words_spaces("Hello World"), "Hello World")
        self.assertEqual(capital_words_spaces("hello world"), "hello world")
        self.assertEqual(capital_words_spaces("hello"), "hello")

    def test_edge(self):
        self.assertEqual(capital_words_spaces(""), "")
        self.assertEqual(capital_words_spaces("Hello"), "Hello")
        self.assertEqual(capital_words_spaces("world"), "world")

    def test_complex(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")
        self.assertEqual(capital_words_spaces("helloWorld"), "hello world")
        self.assertEqual(capital_words_spaces("HelloWorld123"), "Hello World 123")
