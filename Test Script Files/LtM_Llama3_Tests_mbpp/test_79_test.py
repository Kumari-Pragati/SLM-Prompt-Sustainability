import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(word_len("hello world"))

    def test_simple_false(self):
        self.assertFalse(word_len("hello"))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            word_len("")

    def test_single_word(self):
        self.assertFalse(word_len("hello"))

    def test_multiple_words(self):
        self.assertTrue(word_len("hello world abc"))

    def test_single_word_with_spaces(self):
        self.assertFalse(word_len("   hello   "))

    def test_multiple_words_with_spaces(self):
        self.assertTrue(word_len("   hello   world   abc   "))
