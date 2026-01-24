import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        """Test that removing spaces from an empty string returns an empty string."""
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        """Test that removing spaces from a single space string returns an empty string."""
        self.assertEqual(remove_spaces(' '), '')

    def test_multiple_spaces(self):
        """Test that removing spaces from a string with multiple spaces returns the expected result."""
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')

    def test_leading_trailing_spaces(self):
        """Test that leading and trailing spaces are removed."""
        self.assertEqual(remove_spaces('  Hello World  '), 'HelloWorld')

    def test_only_spaces(self):
        """Test that a string of only spaces is converted to an empty string."""
        self.assertEqual(remove_spaces('   '), '')

    def test_non_string_input(self):
        """Test that a non-string input raises a TypeError."""
        with self.assertRaises(TypeError):
            remove_spaces(123)
