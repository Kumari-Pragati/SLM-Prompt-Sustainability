import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_empty_string(self):
        """Test removing a character from an empty string"""
        self.assertEqual(remove_Char("", "a"), "")

    def test_single_character(self):
        """Test removing a single character from a string"""
        self.assertEqual(remove_Char("a", "a"), "")
        self.assertEqual(remove_Char("b", "a"), "b")

    def test_multiple_characters(self):
        """Test removing multiple occurrences of a character from a string"""
        self.assertEqual(remove_Char("aaa", "a"), "")
        self.assertEqual(remove_Char("bbb", "b"), "")
        self.assertEqual(remove_Char("abc", "b"), "ac")

    def test_single_character_in_long_string(self):
        """Test removing a single character from a long string"""
        long_string = "x" * 100
        self.assertEqual(remove_Char(long_string, "x"), "")

    def test_non_existent_character(self):
        """Test removing a non-existent character from a string"""
        self.assertEqual(remove_Char("abc", "d"), "abc")

    def test_string_with_only_non_existent_character(self):
        """Test removing a non-existent character from a string with only that character"""
        self.assertEqual(remove_Char("d", "d"), "")

    def test_string_with_only_existent_character(self):
        """Test removing an existent character from a string with only that character"""
        self.assertEqual(remove_Char("a", "a"), "")
