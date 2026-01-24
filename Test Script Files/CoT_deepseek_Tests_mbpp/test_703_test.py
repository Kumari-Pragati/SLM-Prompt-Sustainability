import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'b'))
        self.assertTrue(is_key_present({'apple': 'fruit', 'banana': 'fruit'}, 'apple'))

    def test_edge_case(self):
        self.assertFalse(is_key_present({}, 'a'))
        self.assertFalse(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'd'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_key_present(123, 'a')
        with self.assertRaises(TypeError):
            is_key_present({'a': 1, 'b': 2, 'c': 3}, 123)
