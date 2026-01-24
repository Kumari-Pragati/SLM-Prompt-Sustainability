import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(is_Isomorphic('egg', 'add'))
        self.assertTrue(is_Isomorphic('paper', 'title'))

    def test_edge_conditions(self):
        self.assertTrue(is_Isomorphic('', ''))
        self.assertFalse(is_Isomorphic('a', ''))
        self.assertFalse(is_Isomorphic('', 'a'))

    def test_boundary_conditions(self):
        self.assertTrue(is_Isomorphic('a'*10000, 'a'*10000))
        self.assertFalse(is_Isomorphic('a'*10001, 'a'*10000))
        self.assertFalse(is_Isomorphic('a'*10000, 'a'*10001))

    def test_complex_cases(self):
        self.assertFalse(is_Isomorphic('foo', 'bar'))
        self.assertFalse(is_Isomorphic('abba', 'abab'))
        self.assertTrue(is_Isomorphic('abba', 'baab'))
