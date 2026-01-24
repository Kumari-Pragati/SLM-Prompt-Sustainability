import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(occurance_substring("hello world", "world"), ("world", 6, 11))

    def test_edge(self):
        self.assertEqual(occurance_substring("hello", "hello"), ("hello", 0, 5))
        self.assertEqual(occurance_substring("hello", "o"), ("o", 4, 4))

    def test_empty(self):
        self.assertIsNone(occurance_substring("", "world"))
        self.assertIsNone(occurance_substring("hello", ""))

    def test_non_match(self):
        self.assertIsNone(occurance_substring("hello", "goodbye"))

    def test_multiple_matches(self):
        self.assertEqual(occurance_substring("hello world hello", "hello"), ("hello", 0, 5))
        self.assertEqual(occurance_substring("hello world hello", "world"), ("world", 6, 11))
