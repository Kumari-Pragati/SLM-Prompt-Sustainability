import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_char('hello', 'l', 'p'), 'heppo')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_char('', 'a', 'b'), '')

    def test_edge_case_no_occurrence(self):
        self.assertEqual(replace_char('hello', 'x', 'y'), 'hello')

    def test_edge_case_same_character(self):
        self.assertEqual(replace_char('hello', 'l', 'l'), 'heelloo')

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            replace_char(None, 'a', 'b')

    def test_invalid_input_non_string_first_arg(self):
        with self.assertRaises(TypeError):
            replace_char(123, 'a', 'b')

    def test_invalid_input_non_string_second_arg(self):
        with self.assertRaises(TypeError):
            replace_char('hello', 123, 'b')

    def test_invalid_input_non_string_third_arg(self):
        with self.assertRaises(TypeError):
            replace_char('hello', 'a', 123)
