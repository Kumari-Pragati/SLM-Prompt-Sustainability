import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_empty_string(self):
        """Test that an empty string returns 0"""
        self.assertEqual(num_position(""), 0)

    def test_single_number(self):
        """Test that a single number returns its index"""
        self.assertEqual(num_position("123"), 0)
        self.assertEqual(num_position("abc123"), 3)
        self.assertEqual(num_position("123abc"), 0)

    def test_multiple_numbers(self):
        """Test that multiple numbers return their indices"""
        self.assertEqual(num_position("123456"), [0, 3, 4, 5])
        self.assertEqual(num_position("abc123def456"), [3, 10])
        self.assertEqual(num_position("123456abc"), [0, 4, 5, 7])

    def test_leading_numbers(self):
        """Test that leading numbers are correctly returned"""
        self.assertEqual(num_position("123abc"), 0)
        self.assertEqual(num_position("abc123"), 3)

    def test_trailing_numbers(self):
        """Test that trailing numbers are correctly returned"""
        self.assertEqual(num_position("abc123"), 3)
        self.assertEqual(num_position("123abc"), 0)

    def test_numbers_in_middle(self):
        """Test that numbers in the middle are correctly returned"""
        self.assertEqual(num_position("abc123def"), [3, 8])
        self.assertEqual(num_position("123abcdef"), [0, 3])

    def test_no_numbers(self):
        """Test that no numbers returns None"""
        self.assertIsNone(num_position("abcdef"))

    def test_non_numeric_characters(self):
        """Test that non-numeric characters are ignored"""
        self.assertEqual(num_position("1a2b3c"), [0, 2])
        self.assertEqual(num_position("1_2_3_"), [0, 2, 4])

    def test_leading_non_numeric_characters(self):
        """Test that leading non-numeric characters are ignored"""
        self.assertEqual(num_position("a1b2c"), [1])
        self.assertEqual(num_position("_123"), [1])

    def test_trailing_non_numeric_characters(self):
        """Test that trailing non-numeric characters are ignored"""
        self.assertEqual(num_position("123a"), [0])
        self.assertEqual(num_position("123_"), [0])
