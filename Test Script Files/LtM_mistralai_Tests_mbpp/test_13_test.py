import unittest
from mbpp_13_code import Counter
from 13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(count_common(['word', 'word', 'another_word', 'word']), [('word', 3)])
        self.assertListEqual(count_common(['word1', 'word2', 'word3', 'word4']), [('word1', 1), ('word2', 1), ('word3', 1), ('word4', 1)])

    def test_edge_cases(self):
        self.assertListEqual(count_common([]), [])
        self.assertListEqual(count_common(['word']), [('word', 1)])
        self.assertListEqual(count_common(['word', 'word', 'word', 'word']), [('word', 4)])
        self.assertListEqual(count_common(['word', 'word', 'word', 'another_word', 'word']), [('word', 3), ('another_word', 1)])

    def test_complex(self):
        self.assertListEqual(count_common(['word1', 'word2', 'word1', 'word3', 'word2', 'word1', 'word4', 'word2']), [('word2', 3), ('word1', 3), ('word3', 1), ('word4', 1)])
        self.assertListEqual(count_common(['word1', 'word2', 'word1', 'word3', 'word2', 'word1', 'word4', 'word2', 'word1']), [('word1', 4), ('word2', 3)])
