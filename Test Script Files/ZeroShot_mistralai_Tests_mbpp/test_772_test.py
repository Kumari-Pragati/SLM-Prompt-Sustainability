import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_length("", 3), "")

    def test_single_word(self):
        self.assertEqual(remove_length("word", 3), "")
        self.assertEqual(remove_length("words", 1), "")
        self.assertEqual(remove_length("word", 2), "word")
        self.assertEqual(remove_length("word", 4), "")

    def test_multiple_words(self):
        self.assertEqual(remove_length("word1 word2 word3", 3), "word3")
        self.assertEqual(remove_length("word1 word2 word3", 2), "word1 word2 word3")
        self.assertEqual(remove_length("word1 word2 word3", 1), "word1 word2 word3")
        self.assertEqual(remove_length("word1 word2 word3", 4), "")

    def test_spaces_only(self):
        self.assertEqual(remove_length("   ", 3), "")
        self.assertEqual(remove_length("   ", 1), "   ")
        self.assertEqual(remove_length("   ", 2), "   ")
