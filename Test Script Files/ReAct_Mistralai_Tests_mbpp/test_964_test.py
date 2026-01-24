import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_empty_string(self):
        """Test if function returns True for an empty string"""
        self.assertTrue(word_len(""))

    def test_single_word(self):
        """Test if function returns True for an odd-length single word"""
        self.assertFalse(word_len("single"))

    def test_single_word_even_length(self):
        """Test if function returns True for an even-length single word"""
        self.assertTrue(word_len("even"))

    def test_multiple_words_odd_length(self):
        """Test if function returns False for multiple words with odd lengths"""
        self.assertFalse(word_len("odd word odd"))

    def test_multiple_words_even_length(self):
        """Test if function returns True for multiple words with even lengths"""
        self.assertTrue(word_len("even word even"))

    def test_mixed_length_words(self):
        """Test if function returns False for a mix of odd and even length words"""
        self.assertFalse(word_len("odd even odd"))

    def test_whitespace_only(self):
        """Test if function returns True for a string containing only whitespace"""
        self.assertTrue(word_len("   "))
