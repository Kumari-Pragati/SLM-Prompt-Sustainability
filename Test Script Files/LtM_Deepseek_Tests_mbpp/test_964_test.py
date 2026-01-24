import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertTrue(word_len("hello world"))
        self.assertFalse(word_len("python"))

    def test_edge_conditions(self):
        self.assertFalse(word_len(""))
        self.assertFalse(word_len("a"))
        self.assertFalse(word_len(" "))

    def test_complex_cases(self):
        self.assertTrue(word_len("even longer word"))
        self.assertFalse(word_len("odd length word"))
