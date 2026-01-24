import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_words_ae_with_a(self):
        self.assertEqual(words_ae("apple banana"), ['apple', 'banana'])

    def test_words_ae_with_e(self):
        self.assertEqual(words_ae("elephant giraffe"), ['elephant', 'giraffe'])

    def test_words_ae_with_ae(self):
        self.assertEqual(words_ae("apple ape banana bear"), ['apple', 'ape', 'banana', 'bear'])

    def test_words_ae_with_no_ae(self):
        self.assertEqual(words_ae("cat dog"), [])

    def test_words_ae_with_empty_string(self):
        self.assertEqual(words_ae(""), [])
