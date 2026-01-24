import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_Repeated_Char("abcde"), 'b')

    def test_edge_case_empty_string(self):
        self.assertEqual(first_Repeated_Char(""), '\0')

    def test_edge_case_single_char(self):
        self.assertEqual(first_Repeated_Char("a"), 'a')

    def test_edge_case_no_repeated_chars(self):
        self.assertEqual(first_Repeated_Char("abcdefg"), '\0')

    def test_edge_case_repeated_chars_at_start(self):
        self.assertEqual(first_Repeated_Char("aaabbb"), 'a')

    def test_edge_case_repeated_chars_at_end(self):
        self.assertEqual(first_Repeated_Char("abcdefgg"), 'g')

    def test_edge_case_repeated_chars_in_middle(self):
        self.assertEqual(first_Repeated_Char("abccdefg"), 'c')

    def test_edge_case_repeated_chars_at_start_and_end(self):
        self.assertEqual(first_Repeated_Char("aaabbbccdd"), 'a')

    def test_edge_case_repeated_chars_everywhere(self):
        self.assertEqual(first_Repeated_Char("aaabbbccdd"), 'a')
