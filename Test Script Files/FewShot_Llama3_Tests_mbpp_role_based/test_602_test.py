import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_repeated_char("abcabc"), 'a')

    def test_edge_case_empty_string(self):
        self.assertEqual(first_repeated_char(""), "None")

    def test_edge_case_single_char_string(self):
        self.assertEqual(first_repeated_char("a"), "None")

    def test_edge_case_no_repeated_char(self):
        self.assertEqual(first_repeated_char("abcdefg"), "None")

    def test_edge_case_repeated_char_at_start(self):
        self.assertEqual(first_repeated_char("aaabc"), 'a')

    def test_edge_case_repeated_char_at_end(self):
        self.assertEqual(first_repeated_char("abcba"), 'a')

    def test_edge_case_repeated_char_in_middle(self):
        self.assertEqual(first_repeated_char("abacaba"), 'a')

    def test_edge_case_repeated_char_at_start_and_end(self):
        self.assertEqual(first_repeated_char("aabcba"), 'a')
