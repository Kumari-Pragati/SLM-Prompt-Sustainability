import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_Char('a'), 'a')
        self.assertEqual(get_Char('z'), 'z')
        self.assertEqual(get_Char('b'), 'b')
        self.assertEqual(get_Char('y'), 'y')
        self.assertEqual(get_Char('c'), 'c')
        self.assertEqual(get_Char('x'), 'x')

    def test_edge(self):
        self.assertEqual(get_Char(''), None)
        self.assertEqual(get_Char(''), None)
        self.assertEqual(get_Char('abc'), 'c')
        self.assertEqual(get_Char('xyz'), 'z')

    def test_complex(self):
        self.assertEqual(get_Char('abcabc'), 'c')
        self.assertEqual(get_Char('xyzxyz'), 'z')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'z')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'z')
