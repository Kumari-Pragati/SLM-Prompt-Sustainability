import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(find_long_word(""), [])

    def test_single_word(self):
        self.assertListEqual(find_long_word("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertListEqual(find_long_word("this is a test"), ["test"])

    def test_long_word_at_beginning(self):
        self.assertListEqual(find_long_word("word1 word2 word3 word4"), ["word4"])

    def test_long_word_at_end(self):
        self.assertListEqual(find_long_word("word1 word2 word3 word"), ["word"])

    def test_long_word_in_middle(self):
        self.assertListEqual(find_long_word("word1 word2 word3 word4 word5"), ["word4"])

    def test_multiple_long_words(self):
        self.assertListEqual(find_long_word("word1word2word3word4word5"), ["word2", "word4"])

    def test_punctuation(self):
        self.assertListEqual(find_long_word("word1,word2.word3!"), ["word2"])

    def test_numbers(self):
        self.assertListEqual(find_long_word("word123word456"), ["word456"])

    def test_mixed_case(self):
        self.assertListEqual(find_long_word("Word1 Word2 Word3 Word4"), ["Word4"])
