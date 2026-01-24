import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_simple_present(self):
        self.assertTrue(is_key_present({'a': 1}, 'a'))

    def test_simple_absent(self):
        self.assertFalse(is_key_present({'a': 1}, 'b'))

    def test_empty_dict(self):
        self.assertFalse(is_key_present({}, 'a'))

    def test_empty_key(self):
        self.assertFalse(is_key_present({'a': 1}, ''))

    def test_dict_with_multiple_keys(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'b'))
        self.assertFalse(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'd'))
