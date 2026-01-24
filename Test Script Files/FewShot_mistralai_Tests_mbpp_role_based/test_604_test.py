import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_whitespace_only(self):
        self.assertEqual(reverse_words("   "), "   ")

    def test_punctuation(self):
        self.assertEqual(reverse_words("hello, world!"), "world! hello,")

    def test_mixed_case(self):
        self.assertEqual(reverse_words("Hello World"), "World Hello")
