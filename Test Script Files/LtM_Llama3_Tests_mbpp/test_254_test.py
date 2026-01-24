import unittest
from mbpp_254_code import words_ae

class TestWordsAe(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(words_ae(""), [])

    def test_single_word(self):
        self.assertEqual(words_ae("hello"), [])

    def test_multiple_words(self):
        self.assertEqual(words_ae("hello world"), [])

    def test_word_with_a(self):
        self.assertEqual(words_ae("apple"), ["apple"])

    def test_word_with_e(self):
        self.assertEqual(words_ae("egg"), ["egg"])

    def test_multiple_words_with_a(self):
        self.assertEqual(words_ae("apple banana"), ["apple", "banana"])

    def test_multiple_words_with_e(self):
        self.assertEqual(words_ae("egg hello"), ["egg", "hello"])

    def test_empty_string_with_a(self):
        self.assertEqual(words_ae("a"), [])

    def test_empty_string_with_e(self):
        self.assertEqual(words_ae("e"), [])

    def test_no_a_or_e(self):
        self.assertEqual(words_ae("hello123"), [])

    def test_a_and_e_together(self):
        self.assertEqual(words_ae("apple egg"), ["apple", "egg"])

    def test_a_and_e_together_with_spaces(self):
        self.assertEqual(words_ae("apple  egg"), ["apple", "egg"])
