import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_empty_string(self):
        """Test if empty string returns False"""
        self.assertFalse(word_len(''))

    def test_single_word(self):
        """Test if single word returns True if odd length"""
        self.assertTrue(word_len('odd_length_word'))
        self.assertFalse(word_len('even_length_word'))

    def test_multiple_words(self):
        """Test if multiple words returns True if any word is odd length"""
        self.assertTrue(word_len('odd_length_word1 even_length_word2'))
        self.assertFalse(word_len('even_length_word1 even_length_word2'))

    def test_whitespace_only(self):
        """Test if whitespace only string returns False"""
        self.assertFalse(word_len('   '))

    def test_single_word_with_whitespace(self):
        """Test if single word with whitespace returns True if odd length"""
        self.assertTrue(word_len(' odd_length_word '))
        self.assertFalse(word_len(' even_length_word '))

    def test_special_characters(self):
        """Test if string with special characters returns True if any word is odd length"""
        self.assertTrue(word_len('!@#$%^&*odd_length_word1 _-even_length_word2'))
        self.assertFalse(word_len('!@#$%^&*even_length_word1 _-even_length_word2'))
