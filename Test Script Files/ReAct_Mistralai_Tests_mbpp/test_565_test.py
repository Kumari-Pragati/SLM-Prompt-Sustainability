import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):

    def test_empty_string(self):
        """Test splitting an empty string"""
        self.assertEqual(split(''), [])

    def test_single_character_string(self):
        """Test splitting a single character string"""
        self.assertEqual(split('a'), ['a'])

    def test_multi_character_string(self):
        """Test splitting a multi-character string"""
        self.assertEqual(split('abc'), ['a', 'b', 'c'])

    def test_whitespace_string(self):
        """Test splitting a string with whitespace"""
        self.assertEqual(split(' Hello World '), ['H', ' ', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', ' '])

    def test_punctuation_string(self):
        """Test splitting a string with punctuation"""
        self.assertEqual(split('Python, the amazing language!'), ['P', 'y', 't', 'h', 'o', 'n', ',', ' ', 't', 'h', 'e', ' ', 'a', 'm', 'a', 'z', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', '!'])

    def test_special_characters_string(self):
        """Test splitting a string with special characters"""
        self.assertEqual(split('123_abc'), ['1', '2', '3', '_', 'a', 'b', 'c'])

    def test_multi_whitespace_string(self):
        """Test splitting a string with multiple whitespaces"""
        self.assertEqual(split('   Hello   World   '), [' ', 'H', ' ', 'e', 'l', 'l', 'o', ' ', ' ', 'W', 'o', 'r', 'l', 'd', ' ', ' ', ' '])
