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
        self.assertEqual(long_words(5, "hello world hello"), ["hello", "world"])

    def test_word_length_greater_than_n(self):
        self.assertEqual(long_words(5, "hello world hello python"), ["world", "python"])

    def test_word_length_less_than_n(self):
        self.assertEqual(long_words(5, "hello world hello python hello"), [])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            long_words(5, 123)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            long_words("five", "hello world")
