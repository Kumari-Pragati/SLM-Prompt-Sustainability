import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_char("hello"), 'o')

    def test_edge_case_empty_string(self):
        self.assertEqual(max_char(""), None)

    def test_edge_case_single_char(self):
        self.assertEqual(max_char("a"), 'a')

    def test_edge_case_all_unique_chars(self):
        self.assertEqual(max_char("abc"), 'a')

    def test_edge_case_all_duplicates(self):
        self.assertEqual(max_char("aaa"), 'a')

    def test_edge_case_multiple_max_chars(self):
        self.assertEqual(max_char("aab"), 'a')

    def test_edge_case_empty_string_with_spaces(self):
        self.assertEqual(max_char("   "), None)

    def test_edge_case_single_char_with_spaces(self):
        self.assertEqual(max_char("a   "), 'a')

    def test_edge_case_all_unique_chars_with_spaces(self):
        self.assertEqual(max_char("a b c"), 'a')

    def test_edge_case_all_duplicates_with_spaces(self):
        self.assertEqual(max_char("a a a"), 'a')

    def test_edge_case_multiple_max_chars_with_spaces(self):
        self.assertEqual(max_char("a a b"), 'a')
