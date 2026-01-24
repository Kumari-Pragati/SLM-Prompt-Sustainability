import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):
    def test_true_return(self):
        self.assertTrue(word_len("hello world"))

    def test_false_return(self):
        self.assertFalse(word_len("hello"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("hello"))

    def test_multiple_words(self):
        self.assertTrue(word_len("hello world this"))

    def test_no_words(self):
        self.assertFalse(word_len("   "))

    def test_spaces(self):
        self.assertFalse(word_len("   hello   "))
