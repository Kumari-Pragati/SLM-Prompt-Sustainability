import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(get_key({}), [])

    def test_single_key_dict(self):
        self.assertEqual(get_key({'a': 1}), ['a'])

    def test_multiple_keys_dict(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'c': 3}), ['a', 'b', 'c'])

    def test_duplicate_keys_dict(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'a': 3}), ['a', 'b', 'a'])
