import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'c': 3}), ['a', 'b', 'c'])

    def test_empty_dict(self):
        self.assertEqual(get_key({}), [])

    def test_single_key_dict(self):
        self.assertEqual(get_key({'a': 1}), ['a'])

    def test_duplicate_keys(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'a': 3}), ['a', 'b'])

    def test_large_dict(self):
        large_dict = {str(i): i for i in range(1000)}
        self.assertEqual(get_key(large_dict), list(large_dict.keys()))
