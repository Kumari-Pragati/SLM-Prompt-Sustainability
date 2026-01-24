import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_max_occuring_char("hello"), 'l')

    def test_edge_case_empty_string(self):
        self.assertEqual(get_max_occuring_char(""), '')

    def test_edge_case_single_char_string(self):
        self.assertEqual(get_max_occuring_char("a"), 'a')

    def test_edge_case_all_unique_chars(self):
        self.assertEqual(get_max_occuring_char("abcdef"), 'a')

    def test_edge_case_all_same_chars(self):
        self.assertEqual(get_max_occuring_char("aaaa"), 'a')

    def test_edge_case_max_occuring_char_at_start(self):
        self.assertEqual(get_max_occuring_char("lll"), 'l')

    def test_edge_case_max_occuring_char_at_end(self):
        self.assertEqual(get_max_occuring_char("llll"), 'l')

    def test_edge_case_max_occuring_char_in_middle(self):
        self.assertEqual(get_max_occuring_char("lll"), 'l')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            get_max_occuring_char(123)
