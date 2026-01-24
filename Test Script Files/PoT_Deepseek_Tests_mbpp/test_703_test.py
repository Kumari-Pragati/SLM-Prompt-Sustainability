import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2}, 'a'))
        self.assertTrue(is_key_present({'apple': 'fruit', 'banana': 'fruit'}, 'apple'))

    def test_edge_case(self):
        self.assertFalse(is_key_present({}, 'a'))
        self.assertFalse(is_key_present({'a': 1}, 'b'))

    def test_boundary_case(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'b'))
        self.assertFalse(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'd'))

    def test_corner_case(self):
        self.assertFalse(is_key_present({'1': 1, '2': 2}, '0'))
        self.assertFalse(is_key_present({'1': 1, '2': 2}, '3'))
