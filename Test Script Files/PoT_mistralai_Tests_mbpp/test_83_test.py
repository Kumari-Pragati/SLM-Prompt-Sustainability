import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_Char('abc'), 'c')
        self.assertEqual(get_Char('z'), 'a')
        self.assertEqual(get_Char('aaa'), 'd')
        self.assertEqual(get_Char('zzz'), 'a')

    def test_edge_cases(self):
        self.assertEqual(get_Char('a'), 'b')
        self.assertEqual(get_Char('zx'), 'y')
        self.assertEqual(get_Char('az'), 'b')
        self.assertEqual(get_Char('zy'), 'a')

    def test_boundary_cases(self):
        self.assertEqual(get_Char(''), ord('a'))
        self.assertEqual(get_Char('a'), ord('b'))
        self.assertEqual(get_Char('z'), ord('a'))
        self.assertEqual(get_Char('aa'), ord('c'))
        self.assertEqual(get_Char('zz'), ord('a'))
