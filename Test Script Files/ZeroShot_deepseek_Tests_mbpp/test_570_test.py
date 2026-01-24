import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_remove_words(self):
        self.assertEqual(remove_words(['hello world', 'python is great'], ['world']), ['hello', 'python is great'])
        self.assertEqual(remove_words(['hello world', 'python is great'], ['world', 'great']), ['hello', 'python is'])
        self.assertEqual(remove_words(['hello world', 'python is great'], ['world', 'great', 'hello']), ['', 'python is'])
        self.assertEqual(remove_words(['hello world', 'python is great'], ['world', 'great', 'hello', 'is']), ['', 'python'])
        self.assertEqual(remove_words(['hello world', 'python is great'], ['world', 'great', 'hello', 'is', 'python']), ['', ''])
