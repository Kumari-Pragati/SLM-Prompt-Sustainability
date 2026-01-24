import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_empty_string(self):
        """Test removing uppercase from an empty string"""
        self.assertEqual(remove_uppercase(""), "")

    def test_all_lowercase(self):
        """Test removing uppercase from a string with all lowercase letters"""
        self.assertEqual(remove_uppercase("hello"), "hello")

    def test_mixed_case(self):
        """Test removing uppercase from a string with mixed case letters"""
        self.assertEqual(remove_uppercase("HeLlO wOrLd"), "helloworld")

    def test_leading_uppercase(self):
        """Test removing uppercase from a string with a leading uppercase letter"""
        self.assertEqual(remove_uppercase("Hello World"), "helloworld")

    def test_trailing_uppercase(self):
        """Test removing uppercase from a string with a trailing uppercase letter"""
        self.assertEqual(remove_uppercase("World"), "world")

    def test_multiple_uppercase(self):
        """Test removing multiple uppercase letters from a string"""
        self.assertEqual(remove_uppercase("HeLLo WoRlD"), "helloworld")

    def test_special_characters(self):
        """Test removing uppercase from a string with special characters"""
        self.assertEqual(remove_uppercase("Hello123@_World"), "hello123@_world")

    def test_numbers(self):
        """Test removing uppercase from a string with numbers"""
        self.assertEqual(remove_uppercase("Hello123"), "hello123")

    def test_error_non_string(self):
        """Test error handling for non-string input"""
        with self.assertRaises(TypeError):
            remove_uppercase(123)
