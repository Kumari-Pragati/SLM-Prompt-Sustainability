import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Repeated_Char("hello"), 'l')
        self.assertEqual(first_Repeated_Char("Python"), 't')
        self.assertEqual(first_Repeated_Char("abcdefghijklmnopqrstuvwxyz"), 'a')

    def test_edge_case_single_char(self):
        self.assertEqual(first_Repeated_Char("a"), 'a')

    def test_edge_case_empty_string(self):
        self.assertEqual(first_Repeated_Char(""), '\0')

    def test_edge_case_no_repeated_chars(self):
        self.assertEqual(first_Repeated_Char("abc"), '\0')

    def test_corner_case_repeated_first_char(self):
        self.assertEqual(first_Repeated_Char("aa"), 'a')
