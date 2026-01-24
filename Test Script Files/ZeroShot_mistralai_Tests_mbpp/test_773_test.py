import unittest
from mbpp_773_code import occurance_substring

class TestOccurrenceSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(occurrence_substring("", ""))

    def test_no_match(self):
        self.assertIsNone(occurrence_substring("Hello", "World"))

    def test_single_match(self):
        result = occurance_substring("Hello World Hello", "Hello")
        self.assertEqual(result[0], "Hello")
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 5)

    def test_multiple_matches(self):
        result = occurance_substring("Hello World Hello World", "Hello")
        self.assertEqual(result[0], "Hello")
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 5)
        result = occurance_substring("Hello World Hello World", "World")
        self.assertEqual(result[0], "World")
        self.assertEqual(result[1], 6)
        self.assertEqual(result[2], 12)
