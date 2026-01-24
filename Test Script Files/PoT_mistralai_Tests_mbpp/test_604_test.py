import unittest
from mbpp_604_code import str

class TestReverseWords(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_edge_case_single_word(self):
        self.assertEqual(reverse_words("word"), "word")

    def test_edge_case_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_edge_case_whitespace(self):
        self.assertEqual(reverse_words("   "), "")

    def test_edge_case_punctuation(self):
        self.assertEqual(reverse_words("hello, world!"), "world! hello,")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(reverse_words("hello   world   "), " world   hello   ")

    def test_corner_case_leading_trailing_whitespace(self):
        self.assertEqual(reverse_words(" hello world "), " world hello ")

    def test_corner_case_leading_trailing_punctuation(self):
        self.assertEqual(reverse_words("!hello world!"), "!world hello!")
