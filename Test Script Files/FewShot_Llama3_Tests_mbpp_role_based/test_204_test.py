import unittest
from mbpp_204_code import count

class TestCount(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count("hello world", "o"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count("", "a"), 0)

    def test_edge_case_single_character_string(self):
        self.assertEqual(count("a", "a"), 1)

    def test_edge_case_single_character_string_with_no_match(self):
        self.assertEqual(count("a", "b"), 0)

    def test_edge_case_single_character_string_with_multiple_matches(self):
        self.assertEqual(count("aa", "a"), 2)

    def test_edge_case_single_character_string_with_no_matches(self):
        self.assertEqual(count("abc", "d"), 0)

    def test_edge_case_single_character_string_with_single_match(self):
        self.assertEqual(count("abc", "b"), 1)

    def test_edge_case_single_character_string_with_multiple_matches(self):
        self.assertEqual(count("abc", "a"), 1)
