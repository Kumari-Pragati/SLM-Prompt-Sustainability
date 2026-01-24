import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(occurance_substring("hello world", "world"), ("world", 6, 11))

    def test_edge_case_start(self):
        self.assertEqual(occurance_substring("hello world", "hello"), ("hello", 0, 5))

    def test_edge_case_end(self):
        self.assertEqual(occurance_substring("hello world", "world"), ("world", 6, 11))

    def test_edge_case_middle(self):
        self.assertEqual(occurance_substring("hello world", "or"), ("or", 4, 5))

    def test_edge_case_no_match(self):
        self.assertIsNone(occurance_subscript("hello world", "abc"))

    def test_edge_case_empty_string(self):
        self.assertIsNone(occurance_substring("", "abc"))

    def test_edge_case_pattern_empty(self):
        self.assertIsNone(occurance_substring("hello world", ""))

    def test_edge_case_text_empty(self):
        self.assertIsNone(occurance_substring("", "world"))

    def test_edge_case_pattern_and_text_empty(self):
        self.assertIsNone(occurance_substring("", ""))
