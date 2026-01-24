import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_capital_words_spaces_simple(self):
        self.assertEqual(capital_words_spaces('HelloWorld'), 'Hello World')

    def test_capital_words_spaces_multiple_capital_letters(self):
        self.assertEqual(capital_words_spaces('HelloWORLD'), 'Hello WORLD')

    def test_capital_words_spaces_no_capital_letters(self):
        self.assertEqual(capital_words_spaces('helloworld'), 'helloworld')

    def test_capital_words_spaces_with_spaces(self):
        self.assertEqual(capital_words_spaces('Hello   WORLD'), 'Hello   WORLD')

    def test_capital_words_spaces_empty_string(self):
        self.assertEqual(capital_words_spaces(''), '')
