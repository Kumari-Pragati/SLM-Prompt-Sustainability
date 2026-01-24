import unittest
from79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(word_len("even length words"))
        self.assertTrue(word_len("odd length word even length word"))

    def test_edge_cases(self):
        self.assertTrue(word_len(""))
        self.assertTrue(word_len("word"))
        self.assertTrue(word_len("word word"))
        self.assertTrue(word_len("word word word"))
        self.assertTrue(word_len("word word word word"))

    def test_boundary_cases(self):
        self.assertFalse(word_len("even length word even"))
        self.assertFalse(word_len("odd length word odd length word"))

    def test_invalid_input(self):
        self.assertFalse(word_len(123))
        self.assertFalse(word_len([]))
        self.assertFalse(word_len([1, 2, 3]))
        self.assertFalse(word_len("123"))
        self.assertFalse(word_len("word,word"))
