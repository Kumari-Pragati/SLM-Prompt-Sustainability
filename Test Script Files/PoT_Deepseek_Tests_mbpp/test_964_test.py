import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(word_len("hello world"))
        self.assertFalse(word_len("hello"))
        self.assertTrue(word_len("evenly spaced words"))

    def test_edge_cases(self):
        self.assertFalse(word_len(""))
        self.assertFalse(word_len(" "))
        self.assertFalse(word_len("a"))

    def test_boundary_conditions(self):
        self.assertTrue(word_len("abcdefgh"))
        self.assertFalse(word_len("abcdefghi"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            word_len(123)
        with self.assertRaises(TypeError):
            word_len(None)
