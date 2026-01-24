import unittest
from79_code import word_len

class TestWordLen(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(word_len("even words only"))
        self.assertTrue(word_len("odd word even word"))

    def test_edge_case_odd_length(self):
        self.assertTrue(word_len("a"))
        self.assertTrue(word_len("ab"))
        self.assertTrue(word_len("abcde"))

    def test_edge_case_even_length(self):
        self.assertFalse(word_len("aa"))
        self.assertFalse(word_len("even"))
        self.assertFalse(word_len("evens"))

    def test_corner_case_empty_string(self):
        self.assertFalse(word_len(""))

    def test_corner_case_single_space(self):
        self.assertFalse(word_len(" "))
