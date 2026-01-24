import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_simple_even_words(self):
        self.assertFalse(word_len("a b c d"))
        self.assertFalse(word_len("a b e d"))

    def test_simple_odd_words(self):
        self.assertTrue(word_len("a b c"))
        self.assertTrue(word_len("a b e"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("a"))
        self.assertTrue(word_len("b"))

    def test_edge_cases(self):
        self.assertFalse(word_len("a b c d e"))
        self.assertTrue(word_len("a b c d e f"))
        self.assertFalse(word_len("a b c d e f g"))
