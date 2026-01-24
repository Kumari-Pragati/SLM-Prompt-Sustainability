import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count("hello world", 'o'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count("", 'o'), 0)

    def test_edge_case_single_character_string(self):
        self.assertEqual(count("a", 'a'), 1)

    def test_edge_case_single_character_string_with_no_match(self):
        self.assertEqual(count("a", 'b'), 0)

    def test_edge_case_single_character_string_with_single_match(self):
        self.assertEqual(count("a", 'a'), 1)

    def test_edge_case_single_character_string_with_multiple_matches(self):
        self.assertEqual(count("aa", 'a'), 2)

    def test_edge_case_single_character_string_with_no_matches(self):
        self.assertEqual(count("a", 'b'), 0)

    def test_edge_case_single_character_string_with_single_non_match(self):
        self.assertEqual(count("a", 'c'), 0)

    def test_edge_case_single_character_string_with_multiple_non_matches(self):
        self.assertEqual(count("aa", 'c'), 0)

    def test_edge_case_single_character_string_with_single_match_and_non_match(self):
        self.assertEqual(count("ac", 'a'), 1)

    def test_edge_case_single_character_string_with_multiple_matches_and_non_matches(self):
        self.assertEqual(count("aac", 'a'), 2)

    def test_edge_case_single_character_string_with_multiple_matches_and_non_matches(self):
        self.assertEqual(count("aac", 'c'), 0)
