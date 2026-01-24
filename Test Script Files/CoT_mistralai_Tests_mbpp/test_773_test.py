import unittest
from mbpp_773_code import occurance_substring

class TestOccurrenceSubstring(unittest.TestCase):
    def test_empty_text(self):
        self.assertIsNone(occurrence_substring('', '.*'))

    def test_empty_pattern(self):
        self.assertIsNone(occurrence_substring('abc', ''))

    def test_single_occurrence(self):
        self.assertEqual(occurrence_substring('abccabca', 'c'), ('c', 1, 3))

    def test_multiple_occurrences(self):
        self.assertEqual(occurrence_substring('abccabca', 'c'), ('c', 1, 3))
        self.assertEqual(occurrence_substring('abccabca', 'a'), ('a', 0, 1))
        self.assertEqual(occurrence_substring('abccabca', 'b'), ('b', 2, 3))
        self.assertEqual(occurrence_substring('abccabca', 'c'), ('c', 1, 3))
        self.assertEqual(occurrence_substring('abccabca', 'cc'), ('cc', 1, 3))

    def test_case_insensitive(self):
        self.assertEqual(occurrence_substring('AbCc', 'c', re.IGNORECASE), ('c', 0, 2))

    def test_boundary_conditions(self):
        self.assertEqual(occurrence_substring('abc', 'a'), ('a', 0, 1))
        self.assertEqual(occurrence_substring('abc', 'b'), None)
        self.assertEqual(occurrence_substring('abc', 'c'), ('c', 1, 3))
        self.assertEqual(occurrence_substring('abc', 'd'), None)
