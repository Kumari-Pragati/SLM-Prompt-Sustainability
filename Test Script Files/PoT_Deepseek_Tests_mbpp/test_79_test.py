import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(word_len("hello world"))
        self.assertFalse(word_len("even length words"))

    def test_edge_cases(self):
        self.assertTrue(word_len("a"))
        self.assertFalse(word_len(""))

    def test_corner_cases(self):
        self.assertTrue(word_len("odd length words with odd length words"))
        self.assertFalse(word_len("even length words with even length words"))
