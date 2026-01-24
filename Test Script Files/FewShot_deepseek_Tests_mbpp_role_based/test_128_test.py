import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(long_words(5, "The quick brown fox jumps"), ['quick', 'brown', 'jumps'])

    def test_edge_case_with_single_word(self):
        self.assertEqual(long_words(5, "word"), [])

    def test_boundary_case_with_exact_length(self):
        self.assertEqual(long_words(5, "abcdef"), ['abcdef'])

    def test_boundary_case_with_one_char_word(self):
        self.assertEqual(long_words(1, "a"), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            long_words("five", "The quick brown fox jumps")

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            long_words(-1, "The quick brown fox jumps")
