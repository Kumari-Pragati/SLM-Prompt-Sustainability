import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(reverse_words("Hello World"), "World Hello")

    def test_single_word(self):
        self.assertEqual(reverse_words("Hello"), "Hello")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_single_space(self):
        self.assertEqual(reverse_words("   "), "   ")

    def test_multiple_spaces(self):
        self.assertEqual(reverse_words("Hello  World"), "World  Hello")

    def test_punctuation(self):
        self.assertEqual(reverse_words("Hello, World!"), "World!, Hello")

    def test_numbers(self):
        self.assertEqual(reverse_words("Hello 123 World"), "World 123 Hello")

    def test_special_chars(self):
        self.assertEqual(reverse_words("Hello @ World"), "World @ Hello")
