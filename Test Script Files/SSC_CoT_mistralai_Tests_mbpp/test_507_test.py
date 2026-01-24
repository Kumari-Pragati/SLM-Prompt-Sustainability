import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(remove_words(['apple', 'banana', 'cherry'], ['apple', 'orange']), ['banana'])
        self.assertListEqual(remove_words(['apple', 'banana', 'cherry'], ['apple', 'banana']), [])

    def test_edge_case_empty_list(self):
        self.assertListEqual(remove_words([], ['apple']), [])

    def test_edge_case_empty_removewords(self):
        self.assertListEqual(remove_words(['apple', 'banana', 'cherry'], []), ['apple', 'banana', 'cherry'])

    def test_edge_case_single_word(self):
        self.assertListEqual(remove_words(['apple'], ['apple']), [])

    def test_edge_case_single_word_in_list(self):
        self.assertListEqual(remove_words(['apple'], ['banana']), ['apple'])

    def test_edge_case_duplicate_words(self):
        self.assertListEqual(remove_words(['apple', 'apple'], ['apple']), [])

    def test_edge_case_duplicate_words_in_list(self):
        self.assertListEqual(remove_words(['apple', 'apple'], ['banana']), ['banana'])
