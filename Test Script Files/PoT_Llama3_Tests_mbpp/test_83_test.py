import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(get_Char("abc"), 'a')
        self.assertEqual(get_Char("xyz"), 'z')
        self.assertEqual(get_Char("abcabc"), 'a')

    def test_edge(self):
        self.assertEqual(get_Char("a"), 'a')
        self.assertEqual(get_Char("z"), 'z')
        self.assertEqual(get_Char("abcabcabc"), 'a')

    def test_boundary(self):
        self.assertEqual(get_Char("b"), 'b')
        self.assertEqual(get_Char("y"), 'y')
        self.assertEqual(get_Char("abcabcab"), 'a')

    def test_corner(self):
        self.assertEqual(get_Char("abcdefghijklmnopqrstuvwxyz"), 'z')
