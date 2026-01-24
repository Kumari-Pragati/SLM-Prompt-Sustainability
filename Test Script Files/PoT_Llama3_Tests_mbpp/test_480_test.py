import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_max_occuring_char("hello"), 'l')

    def test_edge_case_empty_string(self):
        self.assertEqual(get_max_occuring_char(""), '')

    def test_edge_case_single_char(self):
        self.assertEqual(get_max_occuring_char("a"), 'a')

    def test_edge_case_all_same_chars(self):
        self.assertEqual(get_max_occuring_char("aaaa"), 'a')

    def test_edge_case_all_diff_chars(self):
        self.assertEqual(get_max_occuring_char("abc"), 'a')

    def test_edge_case_max_occurrence_at_start(self):
        self.assertEqual(get_max_occuring_char("aaab"), 'a')

    def test_edge_case_max_occurrence_at_end(self):
        self.assertEqual(get_max_occuring_char("bbaaa"), 'a')

    def test_edge_case_max_occurrence_at_middle(self):
        self.assertEqual(get_max_occuring_char("abbaa"), 'a')

    def test_edge_case_max_occurrence_at_start_and_end(self):
        self.assertEqual(get_max_occuring_char("aabbcc"), 'a')

    def test_edge_case_max_occurrence_at_start_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbcc"), 'a')

    def test_edge_case_max_occurrence_at_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbcc"), 'a')

    def test_edge_case_max_occurrence_at_start_and_end_and_middle(self):
        self.assertEqual(get_max_occuring_char("aabbcc"), 'a')
