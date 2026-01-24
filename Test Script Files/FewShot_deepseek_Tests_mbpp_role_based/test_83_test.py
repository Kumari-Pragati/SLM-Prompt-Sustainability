import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Char('abc'), 'd')

    def test_edge_case(self):
        self.assertEqual(get_Char('z'), 'a')

    def test_boundary_case(self):
        self.assertEqual(get_Char('aaa'), 'b')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_Char(123)

    def test_empty_string(self):
        self.assertEqual(get_Char(''), 'a')
