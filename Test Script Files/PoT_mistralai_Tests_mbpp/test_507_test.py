import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], ['word2']), ['word1', 'word3'])
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], ['word1', 'word3']), [])
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], []), ['word1', 'word2', 'word3'])

    def test_edge_case(self):
        self.assertEqual(remove_words(['word'], ['word']), [])
        self.assertEqual(remove_words([], ['word']), [])
        self.assertEqual(remove_words(['word'], []), ['word'])

    def test_corner_case(self):
        self.assertEqual(remove_words(['word', 'word'], ['word', 'word']), [])
        self.assertEqual(remove_words(['word', 'word'], ['word']), ['word'])
        self.assertEqual(remove_words(['word', 'word'], ['word', 'other']), ['other'])
