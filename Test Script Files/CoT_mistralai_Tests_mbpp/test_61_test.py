import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substrings('', 0), 1)

    def test_single_character(self):
        for char in '0123456789':
            self.assertEqual(count_Substrings(char, 1), 1)

    def test_multiple_characters(self):
        for string in ['01', '123', '2345', '34567', '456789']:
            self.assertEqual(count_Substrings(string, len(string)), 1)

    def test_longer_string(self):
        for string in ['0123456789012', '1234567890123', '2345678901234', '3456789012345', '4567890123456', '5678901234567', '6789012345678', '7890123456789', '8901234567890', '9012345678901']:
            self.assertEqual(count_Substrings(string, len(string)), 1)

    def test_negative_sum(self):
        self.assertRaises(ValueError, lambda: count_Substrings('0123', -1))

    def test_non_numeric_characters(self):
        self.assertRaises(ValueError, lambda: count_Substrings('0a1b2c3d4e5f6g7h8i9', 9))
