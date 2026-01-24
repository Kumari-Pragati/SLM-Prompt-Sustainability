import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_char('hello'), 'l')

    def test_edge_case_empty_string(self):
        self.assertEqual(max_char(''), '')

    def test_edge_case_single_char_string(self):
        self.assertEqual(max_char('a'), 'a')

    def test_edge_case_all_unique_chars(self):
        self.assertEqual(max_char('abc'), 'a')

    def test_edge_case_all_same_chars(self):
        self.assertEqual(max_char('aaaa'), 'a')

    def test_edge_case_multiple_max_chars(self):
        self.assertEqual(max_char('abba'), 'a')

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            max_char(123)

    def test_edge_case_non_string_input2(self):
        with self.assertRaises(TypeError):
            max_char([1, 2, 3])
