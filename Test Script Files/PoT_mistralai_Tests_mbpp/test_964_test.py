import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(word_len("even length words"))
        self.assertTrue(word_len("one two three four five"))
        self.assertTrue(word_len("a b c d e"))

    def test_edge_case_odd_length(self):
        self.assertFalse(word_len("odd length word"))
        self.assertFalse(word_len("one two three four five six"))
        self.assertFalse(word_len("a b c d e f"))

    def test_edge_case_single_word(self):
        self.assertFalse(word_len("word"))

    def test_edge_case_empty_string(self):
        self.assertTrue(word_len(""))

    def test_corner_case_empty_word(self):
        self.assertTrue(word_len("   "))
