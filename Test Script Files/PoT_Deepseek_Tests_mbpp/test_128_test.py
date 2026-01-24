import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(long_words(5, "The quick brown fox"), ["quick", "brown", "fox"])

    def test_edge_case_with_single_word(self):
        self.assertEqual(long_words(5, "word"), [])

    def test_boundary_case_with_exact_length(self):
        self.assertEqual(long_words(5, "hello"), [])

    def test_corner_case_with_empty_string(self):
        self.assertEqual(long_words(5, ""), [])

    def test_corner_case_with_long_string(self):
        self.assertEqual(long_words(5, "a"*10000), ["a"*10000])

    def test_corner_case_with_long_words(self):
        self.assertEqual(long_words(5, "a"*6 + " " + "b"*7), ["a"*6, "b"*7])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            long_words(5, 12345)
