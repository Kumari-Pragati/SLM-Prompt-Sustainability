import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_Repeated_Char("abcde"), 'b')

    def test_edge_case_empty_string(self):
        self.assertEqual(first_Repeated_Char(""), '\0')

    def test_edge_case_single_char_string(self):
        self.assertEqual(first_Repeated_Char("a"), 'a')

    def test_edge_case_no_repeated_char(self):
        self.assertEqual(first_Repeated_Char("abcdefg"), '\0')

    def test_edge_case_repeated_char_at_start(self):
        self.assertEqual(first_Repeated_Char("aaabbbcc"), 'a')

    def test_edge_case_repeated_char_at_end(self):
        self.assertEqual(first_Repeated_Char("abcdefgaa"), 'a')

    def test_edge_case_repeated_char_in_middle(self):
        self.assertEqual(first_Repeated_Char("abcba"), 'b')
