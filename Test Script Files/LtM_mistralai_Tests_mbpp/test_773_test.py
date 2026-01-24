import unittest
from mbpp_773_code import occurance_substring

class TestOccurrenceSubstring(unittest.TestCase):

    def test_simple_occurrence(self):
        self.assertEqual(occurrence_substring("hello world", "ll"), ("ll", 2, 4))
        self.assertEqual(occurrence_substring("Python is awesome", "on",), ("on", 7, 10))

    def test_edge_occurrence(self):
        self.assertEqual(occurrence_substring("", "a"), (None, None, None))
        self.assertEqual(occurrence_substring("abc", "abc"), ("abc", 0, 3))
        self.assertEqual(occurrence_substring("abc", "xyz"), (None, None, None))

    def test_boundary_occurrence(self):
        self.assertEqual(occurrence_substring("aaa", "a"), ("a", 0, 1))
        self.assertEqual(occurrence_substring("aaa", "aa"), ("aa", 0, 2))
        self.assertEqual(occurrence_substring("aaa", "aaa"), ("aaa", 0, 3))

    def test_multiple_occurrences(self):
        self.assertEqual(occurrence_substring("aaabbaa", "aa"), (["aa", "aa"], 0, 2, 3))

    def test_case_insensitive(self):
        self.assertEqual(occurrence_substring("PyThOn", "thon"), ("thon", 3, 6))
