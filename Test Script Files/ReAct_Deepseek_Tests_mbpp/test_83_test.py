import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_Char('a'), 'z')
        self.assertEqual(get_Char('b'), 'y')
        self.assertEqual(get_Char('z'), 'a')
        self.assertEqual(get_Char('abc'), 'z')

    def test_edge_cases(self):
        self.assertEqual(get_Char(''), '')
        self.assertEqual(get_Char(' '), ' ')
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'a')

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            get_Char(123)
        with self.assertRaises(TypeError):
            get_Char(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            get_Char({'a': 1})
