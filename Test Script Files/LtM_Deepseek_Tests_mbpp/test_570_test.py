import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_words(['hello world', 'goodbye world'], ['world']), ['hello', 'goodbye'])

    def test_empty_input(self):
        self.assertEqual(remove_words([], ['world']), [])

    def test_edge_case_single_word(self):
        self.assertEqual(remove_words(['world'], ['world']), [])

    def test_multiple_phrases(self):
        self.assertEqual(remove_words(['hello world', 'goodbye world'], ['world']), ['hello', 'goodbye'])

    def test_no_match(self):
        self.assertEqual(remove_words(['hello', 'goodbye'], ['world']), ['hello', 'goodbye'])

    def test_case_sensitivity(self):
        self.assertEqual(remove_words(['Hello world', 'World'], ['world']), ['Hello'])

    def test_multiple_words_to_remove(self):
        self.assertEqual(remove_words(['hello world', 'goodbye world'], ['world', 'hello']), ['goodbye'])

    def test_special_characters(self):
        self.assertEqual(remove_words(['hello, world!', 'goodbye, world!'], ['world']), ['hello,', 'goodbye,'])
