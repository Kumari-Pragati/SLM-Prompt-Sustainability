import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_words([], ['a', 'b']), [])

    def test_single_word(self):
        self.assertEqual(remove_words(['word'], ['a', 'b']), ['word'])

    def test_multiple_words(self):
        self.assertEqual(remove_words(['word1', 'word2', 'word3'], ['a', 'b']), ['word2'])

    def test_multiple_lists(self):
        self.assertEqual(remove_words([['word1', 'a'], ['word2', 'b'], ['word3']], ['a', 'b']), [['word2', 'b']])

    def test_charlist_not_in_words(self):
        self.assertEqual(remove_words(['word1', 'word2'], ['c', 'd']), ['word1', 'word2'])

    def test_charlist_in_words(self):
        self.assertEqual(remove_words(['a-word', 'the-word', 'word'], ['a', 'the']), ['word'])

    def test_charlist_in_prefix(self):
        self.assertEqual(remove_words(['apples', 'oranges', 'bananas'], ['ap', 'or']), ['bananas'])

    def test_charlist_in_suffix(self):
        self.assertEqual(remove_words(['apples', 'oranges', 'bananas'], ['es', 's']), ['apples', 'oranges'])

    def test_charlist_in_middle(self):
        self.assertEqual(remove_words(['apple-word', 'orange-word', 'banana-word'], ['ap', 'an']), ['orange-word'])

    def test_empty_charlist(self):
        self.assertEqual(remove_words(['word1', 'word2'], []), ['word1', 'word2'])

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            remove_words(1, ['a', 'b'])

    def test_invalid_input_charlist(self):
        with self.assertRaises(TypeError):
            remove_words(['word1', 'word2'], 1)
