import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(word_len("even words only"))
        self.assertFalse(word_len("odd words only"))

    def test_edge_cases(self):
        self.assertTrue(word_len("even words only even"))
        self.assertFalse(word_len("odd words only odd"))
        self.assertFalse(word_len("even words only odd"))
        self.assertTrue(word_len("odd words only even"))

    def test_boundary_cases(self):
        self.assertTrue(word_len("even"))
        self.assertFalse(word_len("odd"))
        self.assertFalse(word_len(""))
        self.assertFalse(word_len(" "))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, word_len, 123)
        self.assertRaises(TypeError, word_len, [1, 2, 3])
        self.assertRaises(TypeError, word_len, (1, 2, 3))
        self.assertRaises(TypeError, word_len, {"key": "value"})
