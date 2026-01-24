import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_empty_string(self):
        """Test removing odd characters from an empty string"""
        self.assertEqual(remove_odd(''), '')

    def test_single_character(self):
        """Test removing odd characters from a single character string"""
        for char in ['a', 'b', '0', '9']:
            self.assertEqual(remove_odd(char), char)

    def test_even_length_string(self):
        """Test removing odd characters from a string of even length"""
        for string in ['aa', 'ab', '01', '98']:
            self.assertEqual(remove_odd(string), string)

    def test_odd_length_string(self):
        """Test removing odd characters from a string of odd length"""
        for string in ['a', 'ab', '012', '987']:
            self.assertNotEqual(remove_odd(string), string)
            self.assertEqual(len(remove_odd(string)), len(string) // 2)

    def test_string_with_only_odds(self):
        """Test removing odd characters from a string containing only odd characters"""
        for string in ['13579', 'ABCDEFG', '!@#$%^&*()']:
            self.assertEqual(remove_odd(string), '')
