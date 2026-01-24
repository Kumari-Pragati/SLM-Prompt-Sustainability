import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(occurance_substring("Hello, World!", "World"), ("World", 7, 11))

    def test_edge_case_start(self):
        self.assertEqual(occurance_substring("Hello, World!", "o"), ("o", 4, 5))

    def test_edge_case_end(self):
        self.assertEqual(occurance_substring("Hello, World!", "d"), ("d", 6, 7))

    def test_edge_case_not_found(self):
        self.assertIsNone(occurance_substring("Hello, World!", "abc"))

    def test_edge_case_empty_string(self):
        self.assertIsNone(occurance_substring("", "abc"))

    def test_edge_case_pattern_empty(self):
        self.assertIsNone(occurance_substring("Hello, World!", ""))

    def test_edge_case_text_empty(self):
        self.assertIsNone(occurance_substring("", ""))
