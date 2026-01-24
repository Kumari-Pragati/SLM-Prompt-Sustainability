import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertTrue(is_Isomorphic('egg', 'add'))
        self.assertTrue(is_Isomorphic('paper', 'title'))
        self.assertFalse(is_Isomorphic('foo', 'bar'))
        self.assertFalse(is_Isomorphic('ab', 'aa'))

    def test_edge_cases(self):
        self.assertTrue(is_Isomorphic('', ''))
        self.assertFalse(is_Isomorphic('a', ''))
        self.assertFalse(is_Isomorphic('', 'a'))

    def test_boundary_cases(self):
        self.assertTrue(is_Isomorphic('a'*10000, 'a'*10000))
        self.assertFalse(is_Isomorphic('a'*10000, 'b'*10000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(123, 'abc')
        with self.assertRaises(TypeError):
            is_Isomorphic('abc', 123)
