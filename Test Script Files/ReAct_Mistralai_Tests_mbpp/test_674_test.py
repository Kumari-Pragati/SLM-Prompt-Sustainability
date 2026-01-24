import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_single_word(self):
        self.assertEqual(remove_duplicate('word'), 'word')

    def test_multiple_words(self):
        self.assertEqual(remove_duplicate('word1 word2 word3'), 'word1 word2 word3')

    def test_duplicate_words(self):
        self.assertEqual(remove_duplicate('word1 word1 word2'), 'word1 word2')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_duplicate(' word1 word2 word3 '), 'word1 word2 word3')

    def test_only_spaces(self):
        self.assertEqual(remove_duplicate('   '), '')

    def test_punctuation(self):
        self.assertEqual(remove_duplicate('word1, word2. word3!'), 'word1 word2 word3')

    def test_numbers(self):
        self.assertEqual(remove_duplicate('word1 1word2 2word3'), 'word1 1word2 word3')

    def test_mixed_case(self):
        self.assertEqual(remove_duplicate('Word1 Word2 Word3'), 'Word1 Word2 Word3')

    def test_long_string(self):
        long_string = ' '.join(['word1'] * 100) + ' word2'
        self.assertEqual(remove_duplicate(long_string), 'word1' * 100 + ' word2')
