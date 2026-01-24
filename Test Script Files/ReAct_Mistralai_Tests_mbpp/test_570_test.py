import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(remove_words([], ['a', 'b']), [])

    def test_single_word(self):
        self.assertEqual(remove_words(['word'], ['a', 'b']), ['word'])

    def test_multiple_words(self):
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], ['a', 'b']), ['word2'])

    def test_words_with_characters(self):
        self.assertEqual(remove_words(['worda', 'wordb', 'wordc'], ['a', 'b']), [])

    def test_empty_charlist(self):
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], []), ['word1', 'word2', 'word3'])

    def test_single_char_charlist(self):
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], ['a']), ['word2', 'word3'])

    def test_multiple_chars_charlist(self):
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], ['a', 'b']), ['word3'])

    def test_list_of_lists(self):
        self.assertEqual(remove_words([['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6']], ['a', 'b']),
                         [['word2'], ['word4'], ['word6']])

    def test_list_with_empty_strings(self):
        self.assertEqual(remove_words(['', 'word1', 'word2'], ['a', 'b']), ['word1', 'word2'])

    def test_list_with_only_empty_strings(self):
        self.assertEqual(remove_words([ '', '' ], ['a', 'b']), [])
