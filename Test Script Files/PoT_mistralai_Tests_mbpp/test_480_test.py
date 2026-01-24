import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_max_occuring_char("abcdabcd"), 'c')
        self.assertEqual(get_max_occuring_char("HelloWorld"), 'l')
        self.assertEqual(get_max_occuring_char("1234567890"), '0')

    def test_edge_case_empty_string(self):
        self.assertEqual(get_max_occuring_char(""), '')

    def test_edge_case_single_char(self):
        self.assertEqual(get_max_occuring_char("a"), 'a')

    def test_edge_case_single_digit(self):
        self.assertEqual(get_max_occuring_char("1"), '1')

    def test_edge_case_all_same(self):
        self.assertEqual(get_max_occuring_char("aaaaaa"), 'a')

    def test_edge_case_all_different(self):
        self.assertEqual(get_max_occuring_char("!@#$%^&*()"), '')

    def test_corner_case_whitespace(self):
        self.assertEqual(get_max_occuring_char("   "), ' ')
