import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):

    def test_is_Isomorphic(self):
        self.assertTrue(is_Isomorphic('egg', 'add'))
        self.assertTrue(is_Isomorphic('foo', 'bar'))
        self.assertFalse(is_Isomorphic('paper', 'title'))
        self.assertFalse(is_Isomorphic('abba', 'abcd'))
        self.assertTrue(is_Isomorphic('', ''))
        self.assertFalse(is_Isomorphic('abc', 'abcd'))
