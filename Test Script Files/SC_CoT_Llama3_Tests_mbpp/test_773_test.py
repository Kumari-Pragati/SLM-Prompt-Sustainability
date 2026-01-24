import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(occurance_substring("Hello, world!", "world"), ("world", 7, 11))

    def test_edge_case_start(self):
        self.assertEqual(occurance_substring("Hello, world!", "H"), ("H", 0, 1))

    def test_edge_case_end(self):
        self.assertEqual(occurance_substring("Hello, world!", "ld"), ("ld", 6, 8))

    def test_edge_case_middle(self):
        self.assertEqual(occurance_substring("Hello, world!", "or"), ("or", 4, 6))

    def test_edge_case_no_match(self):
        self.assertIsNone(occurance_substring("Hello, world!", "abc"))

    def test_edge_case_empty_pattern(self):
        self.assertIsNone(occurance_substring("Hello, world!", ""))

    def test_edge_case_empty_text(self):
        self.assertIsNone(occurance_substring("", "world"))

    def test_edge_case_pattern_longer_than_text(self):
        self.assertIsNone(occurance_substring("Hello", "world"))

    def test_edge_case_text_longer_than_pattern(self):
        self.assertEqual(occurance_substring("Hello, world, world", "world"), ("world", 7, 11))
