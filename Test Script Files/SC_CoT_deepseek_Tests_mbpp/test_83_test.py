import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Char('abc'), 'z')

    def test_edge_case(self):
        self.assertEqual(get_Char('z'), 'a')

    def test_boundary_case(self):
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'z')

    def test_special_case(self):
        self.assertEqual(get_Char('xyz'), 'a')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_Char(123)
