import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_long_words(self):
        self.assertEqual(long_words(3, "Hello World"), ["World"])
        self.assertEqual(long_words(5, "Python is fun"), [])
        self.assertEqual(long_words(1, "a b c d e"), ["a", "b", "c", "d", "e"])
        self.assertEqual(long_words(4, "Hello World this is a test"), ["World", "this", "test"])
        self.assertEqual(long_words(7, "Hello World this is a test"), [])

    def test_long_words_empty_string(self):
        self.assertEqual(long_words(3, ""), [])

    def test_long_words_single_word(self):
        self.assertEqual(long_words(3, "Hello"), [])

    def test_long_words_single_word_longer_than_n(self):
        self.assertEqual(long_words(3, "Hello"), ["Hello"])

    def test_long_words_multiple_words(self):
        self.assertEqual(long_words(3, "Hello World this is a test"), ["World", "this", "test"])

    def test_long_words_multiple_words_no_long_words(self):
        self.assertEqual(long_words(5, "Python is fun"), [])
