import unittest

from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_char('hello world', 'l', 'L'), 'heLLo worLD')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_char('', 'a', 'b'), '')

    def test_edge_case_no_match(self):
        self.assertEqual(replace_char('hello world', 'z', 'b'), 'hello world')

    def test_boundary_case_single_character(self):
        self.assertEqual(replace_char('a', 'a', 'b'), 'b')

    def test_special_case_multiple_occurrences(self):
        self.assertEqual(replace_char('hello hello', 'l', 'L'), 'heLLo heLLo')

    def test_invalid_input_none_str1(self):
        with self.assertRaises(TypeError):
            replace_char(None, 'a', 'b')

    def test_invalid_input_none_ch(self):
        with self.assertRaises(TypeError):
            replace_char('hello world', None, 'b')

    def test_invalid_input_none_newch(self):
        with self.assertRaises(TypeError):
            replace_char('hello world', 'a', None)
