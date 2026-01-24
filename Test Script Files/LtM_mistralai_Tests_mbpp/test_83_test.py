import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_Char('a'), 'b')
        self.assertEqual(get_Char('z'), 'a')
        self.assertEqual(get_Char('aa'), 'c')
        self.assertEqual(get_Char('zz'), 'a')

    def test_edge_and_boundary(self):
        self.assertEqual(get_Char(''), ord('z'))
        self.assertEqual(get_Char('a' * 27), 'b')
        self.assertEqual(get_Char('z' * 26), 'a')
        self.assertEqual(get_Char('a' * 26 + 'z'), 'a')
        self.assertEqual(get_Char('z' * 27), ord('a'))

    def test_complex_input(self):
        self.assertEqual(get_Char('abc'), 'd')
        self.assertEqual(get_Char('zyx'), 'a')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), ord('a'))
        self.assertEqual(get_Char('zabcdefghijklmnopqrstuvwxy'), ord('z'))
