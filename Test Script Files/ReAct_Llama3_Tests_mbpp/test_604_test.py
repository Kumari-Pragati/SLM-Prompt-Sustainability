import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(reverse_words("Hello World"), "World Hello")

    def test_single_word(self):
        self.assertEqual(reverse_words("Hello"), "Hello")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_multiple_spaces(self):
        self.assertEqual(reverse_words("Hello  World   Foo"), "World Foo Hello")

    def test_punctuation(self):
        self.assertEqual(reverse_words("Hello, World!"), "World! Hello,")
    def test_non_ascii_characters(self):
        self.assertEqual(reverse_words("Hello, World!"), "World! Hello,")
