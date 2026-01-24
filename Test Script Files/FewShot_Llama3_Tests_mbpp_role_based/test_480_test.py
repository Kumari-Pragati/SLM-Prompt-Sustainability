import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_max_occuring_char("hello"), 'l')

    def test_edge_case_empty_string(self):
        self.assertEqual(get_max_occuring_char(""), '')

    def test_edge_case_single_char_string(self):
        self.assertEqual(get_max_occuring_char("a"), 'a')

    def test_edge_case_all_unique_chars(self):
        self.assertEqual(get_max_occuring_char("abcdefg"), 'a')

    def test_edge_case_all_same_chars(self):
        self.assertEqual(get_max_occuring_char("aaaa"), 'a')

    def test_edge_case_multiple_max_occuring_chars(self):
        self.assertEqual(get_max_occuring_char("aabbcc"), 'a')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            get_max_occuring_char(123)
