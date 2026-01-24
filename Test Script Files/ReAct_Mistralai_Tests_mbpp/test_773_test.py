import unittest
from mbpp_773_code import occurance_substring

class TestOccurrenceSubstring(unittest.TestCase):

    def test_empty_text(self):
        """Test empty text"""
        with self.assertRaises(IndexError):
            occurance_substring("", "abc")

    def test_single_match(self):
        """Test single match"""
        result = occurance_substring("hello world", "world")
        self.assertEqual(result[0], "world")
        self.assertAlmostEqual(result[1], 6)
        self.assertAlmostEqual(result[2], 12)

    def test_multiple_matches(self):
        """Test multiple matches"""
        result = occurance_substring("hello world hello", "hello")
        self.assertEqual(result[0], "hello")
        self.assertAlmostEqual(result[1], 0)
        self.assertAlmostEqual(result[2], 6)
        result = occurance_substring("hello world hello", "world")
        self.assertEqual(result[0], "world")
        self.assertAlmostEqual(result[1], 7)
        self.assertAlmostEqual(result[2], 13)

    def test_no_match(self):
        """Test no match"""
        result = occurance_substring("hello world", "goodbye")
        self.assertIsNone(result)

    def test_pattern_not_string(self):
        """Test pattern not string"""
        with self.assertRaises(TypeError):
            occurance_substring("hello", 123)

    def test_pattern_empty_string(self):
        """Test pattern empty string"""
        with self.assertRaises(ValueError):
            occurance_substring("hello", "")
