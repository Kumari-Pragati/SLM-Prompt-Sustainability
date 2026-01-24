import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(multiple_split(''), [])

    def test_single_word(self):
        self.assertEqual(multiple_split('word'), ['word'])

    def test_multiple_words(self):
        self.assertEqual(multiple_split('word1; word2, word3\* word4\nword5'), ['word1', 'word2', 'word3*', 'word4', 'word5'])

    def test_newline_at_beginning(self):
        self.assertEqual(multiple_split('\nword1; word2, word3\* word4\nword5'), ['word1', 'word2', 'word3*', 'word4', 'word5'])

    def test_newline_at_end(self):
        self.assertEqual(multiple_split('word1; word2, word3\* word4'), ['word1', 'word2', 'word3*', 'word4'])

    def test_newline_in_middle(self):
        self.assertEqual(multiple_split('word1; \nword2, word3\* word4'), ['word1', '', 'word2', 'word3*', 'word4'])

    def test_multiple_newlines(self):
        self.assertEqual(multiple_split('word1; \n\nword2, word3\* word4\n\nword5'), ['word1', '', '', 'word2', 'word3*', 'word4', '', 'word5'])

    def test_special_characters(self):
        self.assertEqual(multiple_split('word1;word2,word3*word4\nword5'), ['word1', 'word2', 'word3*', 'word4', 'word5'])
