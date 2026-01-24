import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(long_words(5, ""), [])

    def test_single_word(self):
        self.assertEqual(long_words(5, "hello"), [])

    def test_multiple_words(self):
        self.assertEqual(long_words(5, "hello world"), ["world"])

    def test_word_length_equal_to_n(self):
        self.assertEqual(long_words(5, "hello world hello"), ["hello"])

    def test_word_length_greater_than_n(self):
        self.assertEqual(long_words(5, "hello world hello world"), ["world", "world"])

    def test_n_is_zero(self):
        self.assertEqual(long_words(0, "hello world"), ["hello", "world"])

    def test_n_is_one(self):
        self.assertEqual(long_words(1, "hello world"), ["hello", "world"])

    def test_n_is_greater_than_word_length(self):
        self.assertEqual(long_words(10, "hello world"), [])

    def test_n_is_negative(self):
        with self.assertRaises(ValueError):
            long_words(-5, "hello world")
