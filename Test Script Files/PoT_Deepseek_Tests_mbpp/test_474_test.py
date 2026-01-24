import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_char("hello world", "l", "L"), "heLLo worLD")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_boundary_case_single_character(self):
        self.assertEqual(replace_char("a", "a", "b"), "b")
        self.assertEqual(replace_char("a", "b", "c"), "a")

    def test_corner_case_no_change(self):
        self.assertEqual(replace_char("hello world", "z", "a"), "hello world")

    def test_corner_case_multiple_occurrences(self):
        self.assertEqual(replace_char("hello hello", "l", "L"), "heLLo heLLo")

    def test_corner_case_case_sensitivity(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "HeLLo")
