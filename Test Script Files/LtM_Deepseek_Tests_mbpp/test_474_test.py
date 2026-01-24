import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(replace_char("hello", "l", "p"), "heppo")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_edge_case_no_occurrence(self):
        self.assertEqual(replace_char("hello", "z", "p"), "hello")

    def test_boundary_case_single_char(self):
        self.assertEqual(replace_char("a", "a", "b"), "b")

    def test_complex_case_multiple_occurrences(self):
        self.assertEqual(replace_char("apple", "p", "z"), "azale")

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            replace_char(None, "a", "b")

    def test_invalid_input_non_string_target(self):
        with self.assertRaises(TypeError):
            replace_char(123, "a", "b")

    def test_invalid_input_non_string_char(self):
        with self.assertRaises(TypeError):
            replace_char("hello", 123, "b")

    def test_invalid_input_non_string_newch(self):
        with self.assertRaises(TypeError):
            replace_char("hello", "a", 123)
