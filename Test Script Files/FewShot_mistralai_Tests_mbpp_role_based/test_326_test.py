import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(most_occurrences(['word']), 'word')

    def test_multiple_words(self):
        self.assertEqual(most_occurrences(['word1', 'word2', 'word1', 'word3', 'word2']), 'word2')

    def test_empty_list(self):
        self.assertIsNone(most_occurrences([]))

    def test_list_with_numbers(self):
        self.assertIsNone(most_occurrences(['1', 'word', '2', 'word']))

    def test_list_with_punctuation(self):
        self.assertIsNone(most_occurrences(['word.', 'word,', 'word!', 'word']))
