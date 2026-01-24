import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Char("hello", 'l'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Char("", 'a'), 0)

    def test_boundary_case_single_character(self):
        self.assertEqual(count_Char("a", 'a'), 1)
        self.assertEqual(count_Char("a", 'b'), 0)

    def test_corner_case_repeated_character(self):
        self.assertEqual(count_Char("aaaa", 'a'), 4)

    def test_corner_case_long_string(self):
        long_string = "a" * 1000
        self.assertEqual(count_Char(long_string, 'a'), 1000)

    def test_corner_case_long_string_with_repetitions(self):
        long_string = "a" * 1000
        self.assertEqual(count_Char(long_string, 'a'), 1000)

    def test_corner_case_long_string_with_repetitions_and_extra(self):
        long_string = "a" * 1000 + "b"
        self.assertEqual(count_Char(long_string, 'a'), 1000)
