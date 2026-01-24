import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(remove_words(['word1', 'word2', 'word3'], ['word2']), ['word1', 'word3'])
        self.assertListEqual(remove_words(['word1', 'word2', 'word3'], ['word1', 'word3']), [])
        self.assertListEqual(remove_words(['word1', 'word2', 'word3'], []), ['word1', 'word2', 'word3'])

    def test_edge_cases(self):
        self.assertListEqual(remove_words([], ['word']), [])
        self.assertListEqual(remove_words(['word'], []), ['word'])
        self.assertListEqual(remove_words(['word'], ['word', 'word']), [])

    def test_boundary_conditions(self):
        self.assertRaises(ValueError, remove_words, [1, 2, 3], ['word'])
        self.assertRaises(TypeError, remove_words, [1, 2, 3], 1)
