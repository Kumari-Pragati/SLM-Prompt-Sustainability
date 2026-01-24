import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_max_occuring_char("hello"), 'l')

    def test_edge_case_empty_string(self):
        self.assertEqual(get_max_occuring_char(""), '')

    def test_edge_case_single_char_string(self):
        self.assertEqual(get_max_occuring_char("a"), 'a')

    def test_edge_case_all_same_chars(self):
        self.assertEqual(get_max_occuring_char("aaaa"), 'a')

    def test_edge_case_all_diff_chars(self):
        self.assertEqual(get_max_occuring_char("abc"), 'a')

    def test_edge_case_max_occuring_char_at_start(self):
        self.assertEqual(get_max_occuring_char("abcabc"), 'a')

    def test_edge_case_max_occuring_char_at_end(self):
        self.assertEqual(get_max_occuring_char("abcba"), 'a')

    def test_edge_case_max_occuring_char_at_middle(self):
        self.assertEqual(get_max_occuring_char("abacab"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end(self):
        self.assertEqual(get_max_occuring_char("aabbcc"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbccaa"), 'a')

    def test_edge_case_max_occuring_char_at_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbccba"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaa"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaab"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabba"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaa"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaab"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabba"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabbaaa"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabbaaaab"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabbaaaabba"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabbaaaabbaaa"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabbaaaabbaaaab"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabbaaaabbaaaabba"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbccbaaaabbaaaabbaaaabbaaaabbaaa"), 'a')

    def test_edge_case_max_occuring_char_at_start_and_end_and_middle_and