import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_empty_string(self):
        """Test empty string"""
        self.assertEqual(remove_length("", K=1), "")

    def test_single_word_same_length(self):
        """Test single word of given length"""
        self.assertEqual(remove_length("word", K=3), "")

    def test_single_word_different_length(self):
        """Test single word of different length"""
        self.assertEqual(remove_length("word", K=2), "word")

    def test_multiple_words_same_length(self):
        """Test multiple words of same length"""
        self.assertEqual(remove_length("one two three", K=3), "")

    def test_multiple_words_different_length(self):
        """Test multiple words of different length"""
        self.assertEqual(remove_length("one two three", K=2), "one three")

    def test_leading_spaces(self):
        """Test leading spaces"""
        self.assertEqual(remove_length(" one two three", K=3), "two three")

    def test_trailing_spaces(self):
        """Test trailing spaces"""
        self.assertEqual(remove_length("one two three ", K=3), "one two")

    def test_negative_length(self):
        """Test negative length"""
        with self.assertRaises(ValueError):
            remove_length("test", K=-1)

    def test_zero_length(self):
        """Test zero length"""
        with self.assertRaises(ValueError):
            remove_length("test", K=0)

    def test_non_string_input(self):
        """Test non-string input"""
        with self.assertRaises(TypeError):
            remove_length(123, K=4)
