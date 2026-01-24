import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_simple_even_length(self):
        self.assertTrue(word_len("a b c d e"))
        self.assertTrue(word_len("z y x w v u"))

    def test_simple_odd_length(self):
        self.assertFalse(word_len("a b c d e f"))
        self.assertFalse(word_len("z y x w v"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertTrue(word_len("a"))
        self.assertFalse(word_len("A"))

    def test_single_word_odd_length(self):
        self.assertFalse(word_len("b"))
        self.assertTrue(word_len("B"))

    def test_spaces_only(self):
        self.assertFalse(word_len("   "))
