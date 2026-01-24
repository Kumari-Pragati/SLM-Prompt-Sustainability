import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_length("", 3), "")

    def test_single_word(self):
        self.assertEqual(remove_length("word", 3), "")

    def test_multiple_words(self):
        self.assertEqual(remove_length("word1 word2 word3", 3), "word1 word3")

    def test_words_of_same_length(self):
        self.assertEqual(remove_length("word1 word2 word3", 4), "")

    def test_words_of_different_lengths(self):
        self.assertEqual(remove_length("word1 word2 word3 word4", 3), "word4")

    def test_words_with_leading_spaces(self):
        self.assertEqual(remove_length(" word1 word2 word3 ", 3), "word1 word3")

    def test_words_with_trailing_spaces(self):
        self.assertEqual(remove_length("word1 word2 word3 ", 3), "word1 word2")

    def test_words_with_spaces_inside(self):
        self.assertEqual(remove_length("word1 word 2 word3", 3), "word1 word3")

    def test_negative_length(self):
        self.assertRaises(ValueError, remove_length, "word", -1)

    def test_zero_length(self):
        self.assertRaises(ValueError, remove_length, "word", 0)
