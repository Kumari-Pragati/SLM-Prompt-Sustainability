import unittest
from964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_even_length_words(self):
        self.assertTrue(word_len("even words example"))

    def test_odd_length_words(self):
        self.assertFalse(word_len("odd words example"))

    def test_single_word(self):
        self.assertTrue(word_len("single word"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_whitespace_only(self):
        self.assertFalse(word_len("   "))

    def test_mixed_length_words(self):
        self.assertTrue(word_len("short word long word"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            word_len(123)
