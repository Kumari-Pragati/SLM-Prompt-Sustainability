import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(word_len("hello world"))

    def test_simple_false(self):
        self.assertFalse(word_len("hello"))

    def test_empty_input(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("hello"))

    def test_multiple_words(self):
        self.assertTrue(word_len("hello world this"))

    def test_mixed_case(self):
        self.assertTrue(word_len("Hello World This"))

    def test_non_alpha_input(self):
        self.assertFalse(word_len("123456"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_len(123)
