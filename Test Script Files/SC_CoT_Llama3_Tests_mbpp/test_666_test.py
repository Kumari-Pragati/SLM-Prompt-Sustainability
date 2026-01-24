import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_char("hello", "l"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count_char("a", "a"), 1)

    def test_edge_case_single_char_string_nonexistent_char(self):
        self.assertEqual(count_char("a", "b"), 0)

    def test_edge_case_single_char_string_char_at_end(self):
        self.assertEqual(count_char("a", "a"), 1)

    def test_edge_case_single_char_string_char_at_start(self):
        self.assertEqual(count_char("a", "a"), 1)

    def test_edge_case_single_char_string_char_in_middle(self):
        self.assertEqual(count_char("abc", "b"), 1)

    def test_edge_case_single_char_string_char_not_found(self):
        self.assertEqual(count_char("abc", "d"), 0)

    def test_edge_case_single_char_string_char_at_start_and_end(self):
        self.assertEqual(count_char("aa", "a"), 2)

    def test_edge_case_single_char_string_char_at_start_and_middle(self):
        self.assertEqual(count_char("aba", "a"), 2)

    def test_edge_case_single_char_string_char_at_end_and_middle(self):
        self.assertEqual(count_char("aba", "a"), 2)

    def test_edge_case_single_char_string_char_at_start_and_end_and_middle(self):
        self.assertEqual(count_char("aab", "a"), 3)

    def test_edge_case_single_char_string_char_at_start_and_end_and_middle_and_start(self):
        self.assertEqual(count_char("aaab", "a"), 4)

    def test_edge_case_single_char_string_char_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(count_char("aaabb", "a"), 5)

    def test_edge_case_single_char_string_char_at_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(count_char("aaabbb", "a"), 6)

    def test_edge_case_single_char_string_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(count_char("aaabbbb", "a"), 7)

    def test_edge_case_single_char_string_char_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(count_char("aaabbbbbb", "a"), 8)
