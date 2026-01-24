import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Isomorphic('egg', 'add'))

    def test_edge_case(self):
        self.assertTrue(is_Isomorphic('', ''))

    def test_boundary_case(self):
        self.assertFalse(is_Isomorphic('a', 'aa'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(123, 'abc')

    def test_different_length_strings(self):
        self.assertFalse(is_Isomorphic('abc', 'abcd'))

    def test_non_isomorphic_strings(self):
        self.assertFalse(is_Isomorphic('foo', 'bar'))
