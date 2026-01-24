import unittest
from mbpp_708_code import Convert

class TestConvertFunction(unittest.TestCase):

    def test_empty_string(self):
        """Test if an empty string returns an empty list"""
        self.assertListEqual(Convert(""), [])

    def test_single_word(self):
        """Test if a single word returns a list with one element"""
        self.assertListEqual(Convert("hello"), ["hello"])

    def test_multiple_words(self):
        """Test if multiple words are correctly split into a list"""
        self.assertListEqual(Convert("hello world"), ["hello", "world"])

    def test_whitespace_only(self):
        """Test if only whitespace returns an empty list"""
        self.assertListEqual(Convert("   "), [])

    def test_leading_trailing_whitespace(self):
        """Test if leading and trailing whitespace is removed"""
        self.assertListEqual(Convert(" hello world   "), ["hello", "world"])

    def test_punctuation(self):
        """Test if punctuation is ignored"""
        self.assertListEqual(Convert("hello, world!"), ["hello", "world"])

    def test_multiple_punctuation(self):
        """Test if multiple punctuation is ignored"""
        self.assertListEqual(Convert("hello., world!?"), ["hello", "world"])

    def test_numbers(self):
        """Test if numbers are correctly split"""
        self.assertListEqual(Convert("1 2 3 4"), [str(i) for i in range(1, 5)])

    def test_mixed_types(self):
        """Test if strings and numbers are correctly split"""
        self.assertListEqual(Convert("1 apple 2 banana 3"), ["1", "apple", "2", "banana"])

    def test_error_non_string(self):
        """Test if a non-string raises a TypeError"""
        with self.assertRaises(TypeError):
            Convert(123)
