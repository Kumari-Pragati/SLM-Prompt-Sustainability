import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):

    def test_uppercase_string(self):
        """Test if is_upper correctly identifies uppercase strings"""
        self.assertTrue(is_upper("HELLO"))

    def test_mixed_case_string(self):
        """Test if is_upper correctly identifies mixed case strings"""
        self.assertFalse(is_upper("Hello"))

    def test_empty_string(self):
        """Test if is_upper correctly identifies empty strings"""
        self.assertIsNone(is_upper(""))

    def test_single_character_string(self):
        """Test if is_upper correctly identifies single character strings"""
        for char in ['A', 'Z', 'a', 'z']:
            self.assertTrue(is_upper(char))

    def test_whitespace_string(self):
        """Test if is_upper correctly identifies whitespace strings"""
        self.assertIsNone(is_upper("   "))

    def test_special_characters_string(self):
        """Test if is_upper correctly identifies strings with special characters"""
        for char in ['!@#$%^&*()_+-=[]{};:'\'<>,.?/']:
            self.assertFalse(is_upper(char))
