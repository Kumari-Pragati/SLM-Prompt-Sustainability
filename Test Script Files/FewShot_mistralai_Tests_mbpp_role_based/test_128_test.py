import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_long_word_single_word(self):
        self.assertEqual(long_words(5, "long word"), ["long", "word"])

    def test_long_word_multiple_words(self):
        self.assertEqual(long_words(3, "short short long short"), ["long", "short"])

    def test_empty_string(self):
        self.assertEqual(long_words(5, ""), [])

    def test_single_character_word(self):
        self.assertEqual(long_words(2, "ab"), [])

    def test_negative_word_length(self):
        self.assertRaises(ValueError, long_words, -1, "long word")
