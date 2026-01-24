import unittest
from mbpp_83_code import get_Char

class TestGet_Char(unittest.TestCase):

    def test_get_Char(self):
        self.assertEqual(get_Char(''), '')
        self.assertEqual(get_Char('a'), 'a')
        self.assertEqual(get_Char('z'), 'a')
        self.assertEqual(get_Char('b'), 'b')
        self.assertEqual(get_Char('y'), 'b')
        self.assertEqual(get_Char('z'), 'a')
        self.assertEqual(get_Char('abc'), 'b')
        self.assertEqual(get_Char('xyz'), 'b')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'a')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'), 'a')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'), 'a')

    def test_get_Char_edge_cases(self):
        self.assertEqual(get_Char(''), '')
        self.assertEqual(get_Char('a'), 'a')
        self.assertEqual(get_Char('z'), 'a')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'a')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'), 'a')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'), 'a')
