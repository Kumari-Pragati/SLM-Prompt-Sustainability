import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):
    def test_even_word_length(self):
        self.assertFalse(word_len("even words"))

    def test_odd_word_length(self):
        self.assertTrue(word_len("odd words"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("word"))

    def test_single_letter(self):
        self.assertFalse(word_len("a"))

    def test_mixed_word_length(self):
        self.assertTrue(word_len("short word long word"))
