import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_char("hello", "l"), 3)
        self.assertEqual(count_char("Python", "n"), 0)
        self.assertEqual(count_char("Aa1Bb2Cc3", "3"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count_char("a", "a"), 1)

    def test_edge_case_single_char_char(self):
        self.assertEqual(count_char("abc", "z"), 0)
