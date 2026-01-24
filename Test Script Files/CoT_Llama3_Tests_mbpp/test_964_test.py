import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_true_return(self):
        self.assertTrue(word_len("hello world"))

    def test_false_return(self):
        self.assertFalse(word_len("hello"))

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            word_len("")

    def test_single_word(self):
        self.assertFalse(word_len("hello"))

    def test_multiple_words(self):
        self.assertTrue(word_len("hello world hello"))

    def test_no_words(self):
        with self.assertRaises(TypeError):
            word_len(None)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_len(123)
