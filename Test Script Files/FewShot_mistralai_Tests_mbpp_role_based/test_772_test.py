import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_remove_single_word(self):
        self.assertEqual(remove_length("word", 1), "word")

    def test_remove_multiple_words(self):
        self.assertEqual(remove_length("word1 word2 word3", 2), "word3")

    def test_remove_all_words(self):
        self.assertEqual(remove_length("word1 word2 word3", 4), "")

    def test_empty_string(self):
        self.assertEqual(remove_length("", 1), "")

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            remove_length("word", -1)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            remove_length("word", 0)
