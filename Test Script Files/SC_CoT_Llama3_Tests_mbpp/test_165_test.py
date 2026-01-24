import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_char_position("Hello World"), 2)

    def test_edge_case_uppercase(self):
        self.assertEqual(count_char_position("ABC"), 0)

    def test_edge_case_lowercase(self):
        self.assertEqual(count_char_position("abc"), 0)

    def test_edge_case_mixed(self):
        self.assertEqual(count_char_position("AbC"), 0)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char_position(""), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(count_char_position("a"), 0)

    def test_edge_case_single_char_uppercase(self):
        self.assertEqual(count_char_position("A"), 0)

    def test_edge_case_single_char_mixed(self):
        self.assertEqual(count_char_position("A"), 0)

    def test_edge_case_single_char_non_alpha(self):
        self.assertEqual(count_char_position("1"), 0)

    def test_edge_case_single_char_non_alpha_uppercase(self):
        self.assertEqual(count_char_position("1"), 0)

    def test_edge_case_single_char_non_alpha_mixed(self):
        self.assertEqual(count_char_position("1"), 0)

    def test_edge_case_multiple_chars_non_alpha(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case_multiple_chars_non_alpha_uppercase(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case_multiple_chars_non_alpha_mixed(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case_multiple_chars_non_alpha_mixed_uppercase(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case_multiple_chars_non_alpha_mixed_lowercase(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case_multiple_chars_non_alpha_mixed_mixed(self):
        self.assertEqual(count_char_position("123"), 0)
