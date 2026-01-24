import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(long_words(5, "this is a test string with words of various lengths"), ["test", "string"])

    def test_edge_cases(self):
        self.assertListEqual(long_words(0, "this is a test string with words of various lengths"), [])
        self.assertListEqual(long_words(len("this"), "this is a test string with words of various lengths"), ["this"])

    def test_boundary_cases(self):
        self.assertListEqual(long_words(1, "this is a test string with words of various lengths"), ["test"])
        self.assertListEqual(long_words(len("this"), "this"), [])

    def test_empty_string(self):
        self.assertListEqual(long_words(5, ""), [])

    def test_single_word(self):
        self.assertListEqual(long_words(5, "longword"), [])

    def test_single_character(self):
        self.assertListEqual(long_words(5, "a"), [])

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            long_words(-1, "this is a test string with words of various lengths")
