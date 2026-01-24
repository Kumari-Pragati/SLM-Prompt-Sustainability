import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(long_words(5, "Hello World"), ["Hello", "World"])

    def test_edge_case_short_words(self):
        self.assertEqual(long_words(10, "short words"), [])

    def test_edge_case_single_long_word(self):
        self.assertEqual(long_words(5, "supercalifragilisticexpialidocious"), ["supercalifragilisticexpialidocious"])

    def test_edge_case_empty_string(self):
        self.assertEqual(long_words(5, ""), [])

    def test_edge_case_long_words_in_string(self):
        self.assertEqual(long_words(5, "supercalifragilisticexpialidocious is a long word"), ["supercalifragilisticexpialidocious", "long"])

    def test_edge_case_negative_length(self):
        with self.assertRaises(ValueError):
            long_words(-1, "Hello World")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            long_words(5, 12345)
