import unittest
from mbpp_83_code import get_Char

class TestGet_Char(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_Char("abc"), 'c')

    def test_edge_case_lowercase(self):
        self.assertEqual(get_Char("z"), 'z')

    def test_edge_case_uppercase(self):
        self.assertEqual(get_Char("Z"), 'z')

    def test_edge_case_empty_string(self):
        self.assertEqual(get_Char(""), 'a')

    def test_edge_case_single_character(self):
        self.assertEqual(get_Char("a"), 'a')

    def test_edge_case_multiple_characters(self):
        self.assertEqual(get_Char("abcde"), 'e')

    def test_edge_case_long_string(self):
        self.assertEqual(get_Char("abcdefghijklmnopqrstuvwxyz"), 'z')

    def test_edge_case_repeated_characters(self):
        self.assertEqual(get_Char("aaabbbccc"), 'c')

    def test_edge_case_non_ascii_characters(self):
        self.assertEqual(get_Char("abc123"), 'c')

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            get_Char(123)
