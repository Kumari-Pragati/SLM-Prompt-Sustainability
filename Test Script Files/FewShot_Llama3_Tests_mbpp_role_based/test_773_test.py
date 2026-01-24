import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):
    def test_typical_use_case(self):
        text = "Hello, world! Hello, world!"
        pattern = "world"
        result = occurance_substring(text, pattern)
        self.assertEqual(result[0], "world")
        self.assertEqual(result[1], 7)
        self.assertEqual(result[2], 11)

    def test_multiple_occurrences(self):
        text = "Hello, world! Hello, world! Hello, world!"
        pattern = "world"
        result = occurance_substring(text, pattern)
        self.assertEqual(result[0], "world")
        self.assertEqual(result[1], 7)
        self.assertEqual(result[2], 11)
        self.assertEqual(result[3][0], "world")
        self.assertEqual(result[3][1], 18)
        self.assertEqual(result[3][2], 22)

    def test_single_occurrence(self):
        text = "Hello, world!"
        pattern = "world"
        result = occurance_substring(text, pattern)
        self.assertEqual(result[0], "world")
        self.assertEqual(result[1], 7)
        self.assertEqual(result[2], 11)

    def test_no_occurrences(self):
        text = "Hello, hello!"
        pattern = "world"
        result = occurance_substring(text, pattern)
        self.assertIsNone(result)

    def test_empty_text(self):
        text = ""
        pattern = "world"
        result = occurance_substring(text, pattern)
        self.assertIsNone(result)

    def test_empty_pattern(self):
        text = "Hello, world!"
        pattern = ""
        result = occurance_substring(text, pattern)
        self.assertIsNone(result)
