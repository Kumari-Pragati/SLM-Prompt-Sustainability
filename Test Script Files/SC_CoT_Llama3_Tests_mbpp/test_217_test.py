import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(first_Repeated_Char("abcde"), 'b')

    def test_edge_case_empty_string(self):
        self.assertEqual(first_Repeated_Char(""), '\0')

    def test_edge_case_single_char_string(self):
        self.assertEqual(first_Repeated_Char("a"), 'a')

    def test_edge_case_all_unique_chars(self):
        self.assertEqual(first_Repeated_Char("abcdefg"), '\0')

    def test_edge_case_all_repeated_chars(self):
        self.assertEqual(first_Repeated_Char("aaabbbcc"), 'a')

    def test_edge_case_repeated_chars_at_beginning(self):
        self.assertEqual(first_Repeated_Char("aaabbbccdef"), 'a')

    def test_edge_case_repeated_chars_at_end(self):
        self.assertEqual(first_Repeated_Char("abcdefgaaabbbcc"), 'a')

    def test_edge_case_repeated_chars_at_beginning_and_end(self):
        self.assertEqual(first_Repeated_Char("aaabbbccdefaaabbbcc"), 'a')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            first_Repeated_Char(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            first_Repeated_Char(None)
