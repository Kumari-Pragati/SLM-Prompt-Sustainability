import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_char_position("Hello World"), 2)

    def test_edge_case_lowercase(self):
        self.assertEqual(count_char_position("hello world"), 2)

    def test_edge_case_uppercase(self):
        self.assertEqual(count_char_position("HELLO WORLD"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char_position(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(count_char_position("a"), 1)

    def test_edge_case_single_character_uppercase(self):
        self.assertEqual(count_char_position("A"), 1)

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(count_char_position("   "), 0)

    def test_edge_case_non_alphabetic_characters(self):
        self.assertEqual(count_char_position("Hello!"), 2)
