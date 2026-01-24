import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_Char('a'), 'z')
        self.assertEqual(get_Char('b'), 'a')
        self.assertEqual(get_Char('c'), 'b')
        self.assertEqual(get_Char('z'), 'y')

    def test_edge_conditions(self):
        self.assertEqual(get_Char(''), '')
        self.assertEqual(get_Char(' '), ' ')
        self.assertEqual(get_Char('aa'), 'z')
        self.assertEqual(get_Char('ab'), 'a')
        self.assertEqual(get_Char('ba'), 'z')
        self.assertEqual(get_Char('abc'), 'b')

    def test_complex_cases(self):
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'z')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyza'), 'z')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyzab'), 'z')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyzabc'), 'z')
