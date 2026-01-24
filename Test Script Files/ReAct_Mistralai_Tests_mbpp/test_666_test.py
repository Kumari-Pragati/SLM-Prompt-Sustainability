import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_empty_string(self):
        """Test counting a character in an empty string"""
        self.assertEqual(count_char("", "a"), 0)

    def test_single_character(self):
        """Test counting a single character"""
        self.assertEqual(count_char("a", "a"), 1)

    def test_multiple_characters(self):
        """Test counting multiple occurrences of a character"""
        self.assertEqual(count_char("aaa", "a"), 3)

    def test_case_insensitive(self):
        """Test counting a character regardless of case"""
        self.assertEqual(count_char("Aa1Bb2ccCdD", "a"), 3)

    def test_boundary_case_long_string(self):
        """Test counting a character in a long string"""
        self.assertEqual(count_char("x" * 1000, "x"), 1000)

    def test_boundary_case_single_character(self):
        """Test counting a character in a string of length 1"""
        self.assertEqual(count_char("a", "a"), 1)

    def test_error_non_string_input(self):
        """Test error handling for non-string input"""
        with self.assertRaises(TypeError):
            count_char(123, "a")

    def test_error_non_existing_character(self):
        """Test error handling for a non-existing character"""
        with self.assertRaises(ValueError):
            count_char("abc", "x")
