import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_empty_string(self):
        """Test counting a character in an empty string"""
        self.assertEqual(count("", "a"), 0)

    def test_single_character(self):
        """Test counting a single character"""
        self.assertEqual(count("a", "a"), 1)

    def test_multiple_characters(self):
        """Test counting multiple instances of a character"""
        self.assertEqual(count("aaa", "a"), 3)

    def test_case_insensitive(self):
        """Test counting a character regardless of case"""
        self.assertEqual(count("Aa1", "a"), 1)

    def test_boundary_case_long_string(self):
        """Test counting a character in a long string"""
        self.assertEqual(count("abcdefghijklmnopqrstuvwxyz", "z"), 1)

    def test_boundary_case_single_character(self):
        """Test counting a single character in a string"""
        self.assertEqual(count("z", "z"), 1)

    def test_non_existent_character(self):
        """Test counting a non-existent character"""
        self.assertEqual(count("abc", "d"), 0)

    def test_negative_string_length(self):
        """Test handling a negative string length"""
        self.assertRaises(IndexError, lambda: count("-1", "a"))
