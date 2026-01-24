import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(long_words(5, ""), [])

    def test_no_words_longer_than_n(self):
        self.assertEqual(long_words(5, "hello world"), [])

    def test_single_word_longer_than_n(self):
        self.assertEqual(long_words(5, "hello"), ["hello"])

    def test_multiple_words_longer_than_n(self):
        self.assertEqual(long_words(5, "hello world abc"), ["hello", "world"])

    def test_multiple_words_with_various_lengths(self):
        self.assertEqual(long_words(5, "hello world abc def"), ["hello", "world", "def"])

    def test_n_is_zero(self):
        with self.assertRaises(ValueError):
            long_words(0, "hello world")

    def test_n_is_negative(self):
        with self.assertRaises(ValueError):
            long_words(-5, "hello world")
