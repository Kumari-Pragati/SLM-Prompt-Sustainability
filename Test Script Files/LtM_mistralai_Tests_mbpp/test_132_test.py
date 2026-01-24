import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):

    def test_simple_string_tuple(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(tup_string(('x',)), 'x')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            tup_string((1, 'a', 3.14))

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            tup_string((1, 2, 3))

    def test_large_tuple(self):
        self.assertEqual(tup_string(tuple('abcdefghijklmnopqrstuvwxyz')), 'abcdefghijklmnopqrstuvwxyz')
