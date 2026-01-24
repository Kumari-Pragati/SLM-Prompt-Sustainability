import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(long_words(5, "The quick brown fox jumps"), ['quick', 'brown', 'jumps'])

    def test_single_long_word(self):
        self.assertEqual(long_words(5, "longword"), ['longword'])

    def test_no_long_words(self):
        self.assertEqual(long_words(5, "short short"), [])

    def test_empty_string(self):
        self.assertEqual(long_words(5, ""), [])

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            long_words(-1, "The quick brown fox jumps")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            long_words(5, 12345)

    def test_zero_length(self):
        self.assertEqual(long_words(0, "The quick brown fox jumps"), [])
