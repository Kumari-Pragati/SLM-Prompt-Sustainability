import unittest
from mbpp_83_code import get_Char

class TestGet_Char(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(get_Char("abc"), 'a')
        self.assertEqual(get_Char("xyz"), 'z')
        self.assertEqual(get_Char("abcabc"), 'a')

    def test_edge_cases(self):
        self.assertEqual(get_Char(""), 'a')
        self.assertEqual(get_Char("a"), 'a')
        self.assertEqual(get_Char("z"), 'z')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_Char(123)
        with self.assertRaises(TypeError):
            get_Char([1, 2, 3])
        with self.assertRaises(TypeError):
            get_Char({"a": 1})

    def test_boundary_conditions(self):
        self.assertEqual(get_Char("abcdefghijklmnopqrstuvwxyz"), 'a')
        self.assertEqual(get_Char("zabcdefghijklmnopqrstuvwxyz"), 'a')
