import unittest
from mbpp_773_code import occurance_substring

class TestOccurrenceSubstring(unittest.TestCase):
    def test_occurrence_single_substring(self):
        self.assertEqual(occurrence_substring("Hello World", "World"), ("World", 6, 11))

    def test_occurrence_multiple_substrings(self):
        self.assertEqual(occurrence_substring("Hello World Hello", "Hello"), [("Hello", 0, 5), ("Hello", 12, 17)])

    def test_occurrence_empty_string(self):
        self.assertEqual(occurrence_substring("", "World"), [])

    def test_occurrence_substring_not_found(self):
        self.assertEqual(occurrence_substring("Hello World", "X"), [])

    def test_occurrence_substring_with_spaces(self):
        self.assertEqual(occurrence_substring("Hello World", " World"), [("World", 6, 11)])

    def test_occurrence_substring_with_special_characters(self):
        self.assertEqual(occurrence_substring("Hello@World", "@"), [("@", 4, 5)])
