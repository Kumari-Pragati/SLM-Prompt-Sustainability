import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Isomorphic('egg', 'add'))
        self.assertTrue(is_Isomorphic('paper', 'title'))
        self.assertFalse(is_Isomorphic('foo', 'bar'))

    def test_empty_strings(self):
        self.assertTrue(is_Isomorphic('', ''))

    def test_single_character_strings(self):
        self.assertTrue(is_Isomorphic('a', 'a'))
        self.assertFalse(is_Isomorphic('a', 'b'))

    def test_edge_cases(self):
        self.assertFalse(is_Isomorphic('ab', 'aa'))
        self.assertFalse(is_Isomorphic('ab', 'ba'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(123, 'abc')
        with self.assertRaises(TypeError):
            is_Isomorphic('abc', 123)
        with self.assertRaises(TypeError):
            is_Isomorphic(123, 456)
