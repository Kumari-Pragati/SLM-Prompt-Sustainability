import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_empty_string(self):
        """Test minimum length for empty string"""
        self.assertEqual(minimum_Length(''), 0)

    def test_single_letter(self):
        """Test minimum length for single letter"""
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(minimum_Length(char), 1)

    def test_multiple_letters(self):
        """Test minimum length for multiple letters"""
        for length in range(1, 27):
            for letters in 'a' * length + 'z' * (26 - length):
                self.assertEqual(minimum_Length(letters), 1)

    def test_mixed_case(self):
        """Test minimum length for mixed case strings"""
        for letters in ('AaBbCc', '1234567890', '!@#$%^&*()'):
            self.assertEqual(minimum_Length(letters), 1)

    def test_long_string(self):
        """Test minimum length for long strings"""
        for length in range(27, 100):
            for letters in 'a' * length + 'z' * (26 - length):
                self.assertEqual(minimum_Length(letters), 1)

    def test_max_length(self):
        """Test minimum length for maximum length string"""
        self.assertEqual(minimum_Length('z' * 26), 0)

    def test_non_alphabet_characters(self):
        """Test minimum length for strings with non-alphabet characters"""
        for characters in ('!@#$%^&*()1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'):
            self.assertRaises(ValueError, minimum_Length, characters)
