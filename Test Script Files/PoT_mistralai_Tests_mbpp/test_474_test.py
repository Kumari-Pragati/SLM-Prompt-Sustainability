import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "Hello")
        self.assertEqual(replace_char("World", "o", "X"), "WXld")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_edge_case_single_char(self):
        self.assertEqual(replace_char("a", "a", "b"), "b")

    def test_edge_case_single_char_in_string(self):
        self.assertEqual(replace_char("ab", "a", "b"), "b")

    def test_boundary_case_start_of_string(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "Hello")
        self.assertEqual(replace_char("Hello", "H", "L"), "Lello")

    def test_boundary_case_end_of_string(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "Hello")
        self.assertEqual(replace_char("Hello", "o", "L"), "HelloL")

    def test_boundary_case_middle_of_string(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "Hello")
        self.assertEqual(replace_char("Hello", "e", "L"), "HellLo")
