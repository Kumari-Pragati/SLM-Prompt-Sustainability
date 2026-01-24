import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(word_len("hello world"))

    def test_edge_case(self):
        self.assertFalse(word_len("a"))

    def test_special_case(self):
        self.assertTrue(word_len("evenly spaced words"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            word_len(123)
