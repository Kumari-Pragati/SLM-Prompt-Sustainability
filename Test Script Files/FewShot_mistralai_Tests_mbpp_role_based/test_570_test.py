import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_words([], []), [])

    def test_empty_charlist(self):
        self.assertEqual(remove_words(["word1", "word2"], []), ["word1", "word2"])

    def test_single_word(self):
        self.assertEqual(remove_words(["word"], []), ["word"])

    def test_multiple_words(self):
        self.assertEqual(remove_words(["word1", "word2", "word3"], []), ["word1", "word2", "word3"])

    def test_single_char_charlist(self):
        self.assertEqual(remove_words(["word1", "word2"], ["a"]), ["word1", "word2"])

    def test_multiple_chars_charlist(self):
        self.assertEqual(remove_words(["word1", "word2"], ["a", "b"]), ["word1", "word2"])

    def test_char_in_word(self):
        self.assertEqual(remove_words(["worda", "wordb"], ["a"]), ["wordb"])

    def test_multiple_chars_in_word(self):
        self.assertEqual(remove_words(["wordaa", "wordab"], ["a"]), ["wordab"])

    def test_charlist_in_word(self):
        self.assertEqual(remove_words(["wordab", "wordac"], ["a", "b"]), [])
