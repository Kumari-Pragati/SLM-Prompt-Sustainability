import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(word_len("Hello World"))

    def test_even_length_word(self):
        self.assertTrue(word_len("Hello"))

    def test_odd_length_word(self):
        self.assertFalse(word_len("HelloWorld"))

    def test_multiple_words(self):
        self.assertTrue(word_len("Hello World Foo"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_space(self):
        self.assertFalse(word_len(" "))

    def test_multiple_spaces(self):
        self.assertFalse(word_len("   "))

    def test_no_words(self):
        self.assertFalse(word_len("   "))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_len(123)

    def test_non_string_input2(self):
        with self.assertRaises(TypeError):
            word_len([1, 2, 3])
