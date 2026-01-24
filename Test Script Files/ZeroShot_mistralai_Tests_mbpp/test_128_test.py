import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(long_words(5, ""), [])

    def test_single_word(self):
        self.assertListEqual(long_words(5, "short word"), ["short word"])

    def test_multiple_words(self):
        self.assertListEqual(long_words(5, "long word short word very long word"), ["long word", "very long word"])

    def test_long_word_at_beginning(self):
        self.assertListEqual(long_words(5, "very long word short word"), ["very long word"])

    def test_long_word_at_end(self):
        self.assertListEqual(long_words(5, "short word very long word"), ["very long word"])

    def test_long_word_in_middle(self):
        self.assertListEqual(long_words(5, "short word long word short word"), ["long word"])

    def test_long_word_equal_n(self):
        self.assertListEqual(long_words(5, "word1 word2 word3 word4 word5"), ["word5"])
