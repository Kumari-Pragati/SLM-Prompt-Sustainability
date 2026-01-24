import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Char("hello", 'l'), 3)
        self.assertEqual(count_Char("Python", 't'), 1)
        self.assertEqual(count_Char("12345", '5'), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Char("", 'a'), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(count_Char("a", 'a'), 1)

    def test_edge_case_long_string(self):
        long_str = 'a' * 1000
        self.assertEqual(count_Char(long_str, 'a'), 1000)

    def test_edge_case_single_char_in_long_string(self):
        long_str = 'a' * 1000 + 'b'
        self.assertEqual(count_Char(long_str, 'a'), 1000)
        self.assertEqual(count_Char(long_str, 'b'), 1)

    def test_corner_case_no_match(self):
        self.assertEqual(count_Char("hello", 'x'), 0)
