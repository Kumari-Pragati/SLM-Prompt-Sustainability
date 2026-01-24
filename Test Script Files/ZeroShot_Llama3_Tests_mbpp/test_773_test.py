import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_occurrence_substring(self):
        self.assertEqual(occurance_substring("Hello, World!", "World"), ("World", 7, 11))
        self.assertEqual(occurance_substring("Hello, World!", "hello"), ("hello", 0, 6))
        self.assertEqual(occurance_substring("Hello, World!", "world"), None)
        self.assertEqual(occurance_substring("Hello, World!", "Worlds"), None)
        self.assertEqual(occurance_substring("Hello, World!", "Worlds"), None)
        self.assertEqual(occurance_substring("Hello, World!", "Wor"), ("Wor", 7, 9))
        self.assertEqual(occurance_substring("Hello, World!", "wor"), None)

    def test_occurrence_substring_empty_string(self):
        self.assertEqual(occurance_substring("", "World"), None)

    def test_occurrence_substring_empty_pattern(self):
        self.assertEqual(occurance_substring("Hello, World!", ""), None)

    def test_occurrence_substring_pattern_not_found(self):
        self.assertEqual(occurance_substring("Hello, World!", "Unfound"), None)
