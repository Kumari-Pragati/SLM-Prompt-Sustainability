import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_multiple_spaces(self):
        self.assertEqual(reverse_words("   hello   world   "), "world hello")

    def test_punctuation(self):
        self.assertEqual(reverse_words("Hello, world!"), "world, Hello!")

    def test_numbers(self):
        self.assertEqual(reverse_words("Hello 123 world"), "world 123 Hello")

    def test_special_characters(self):
        self.assertEqual(reverse_words("Hello!@# world"), "world!@# Hello")
