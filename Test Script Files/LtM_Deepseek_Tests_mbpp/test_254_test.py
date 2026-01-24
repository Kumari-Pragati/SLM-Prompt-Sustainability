import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_simple_words(self):
        self.assertEqual(words_ae("apple aeroplane"), ['apple', 'aeroplane'])

    def test_single_letter_words(self):
        self.assertEqual(words_ae("a e i o u"), ['a', 'e', 'i', 'o', 'u'])

    def test_empty_string(self):
        self.assertEqual(words_ae(""), [])

    def test_no_ae_letters(self):
        self.assertEqual(words_ae("bcdfghjklmnpqrstvwxyz"), [])

    def test_words_with_ae_at_end(self):
        self.assertEqual(words_ae("apple aeroplane"), ['apple', 'aeroplane'])

    def test_words_with_ae_at_start(self):
        self.assertEqual(words_ae("aeroplane apple"), ['aeroplane', 'apple'])

    def test_words_with_ae_in_middle(self):
        self.assertEqual(words_ae("apple aeroplane"), ['apple', 'aeroplane'])

    def test_words_with_ae_at_both_ends(self):
        self.assertEqual(words_ae("aeroplane apple"), ['aeroplane', 'apple'])
