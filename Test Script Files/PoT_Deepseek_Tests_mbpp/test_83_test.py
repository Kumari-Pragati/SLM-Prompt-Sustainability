import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_Char('abc'), 'c')
        self.assertEqual(get_Char('xyz'), 'z')
        self.assertEqual(get_Char('hello'), 'm')

    def test_edge_cases(self):
        self.assertEqual(get_Char(''), 'a')
        self.assertEqual(get_Char('a'), 'z')
        self.assertEqual(get_Char('z'), 'z')

    def test_boundary_cases(self):
        self.assertEqual(get_Char('ab'), 'c')
        self.assertEqual(get_Char('yz'), 'z')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'a')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_Char(123)
        with self.assertRaises(TypeError):
            get_Char(None)
        with self.assertRaises(TypeError):
            get_Char(['a', 'b', 'c'])
