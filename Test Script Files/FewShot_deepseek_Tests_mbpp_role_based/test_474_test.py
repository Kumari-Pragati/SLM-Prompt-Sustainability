import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_char('hello', 'l', 'p'), 'heppo')

    def test_edge_condition(self):
        self.assertEqual(replace_char('', 'a', 'b'), '')

    def test_boundary_condition(self):
        self.assertEqual(replace_char('a' * 10000, 'a', 'b'), 'b' * 10000)

    def test_no_occurrence(self):
        self.assertEqual(replace_char('hello', 'x', 'y'), 'hello')

    def test_replace_all_occurrences(self):
        self.assertEqual(replace_char('aaa', 'a', 'b'), 'bbb')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_char(123, 'a', 'b')
