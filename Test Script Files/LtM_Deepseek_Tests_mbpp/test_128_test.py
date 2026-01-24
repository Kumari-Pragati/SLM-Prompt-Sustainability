import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(long_words(3, "the quick brown fox"), ["brown", "quick"])

    def test_edge_case_empty_string(self):
        self.assertEqual(long_words(3, ""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(long_words(3, "word"), [])

    def test_edge_case_short_words(self):
        self.assertEqual(long_words(5, "short words"), [])

    def test_boundary_case_exact_length(self):
        self.assertEqual(long_words(4, "four letter"), ["letter"])

    def test_complex_case_mixed_lengths(self):
        self.assertEqual(long_words(4, "short long words are here"), ["long", "words", "are", "here"])
