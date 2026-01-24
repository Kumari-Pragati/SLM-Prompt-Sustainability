import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_key({'a': 1, 'b': 2}), ['a', 'b'])

    def test_empty_input(self):
        self.assertEqual(get_key({}), [])

    def test_single_key_input(self):
        self.assertEqual(get_key({'c': 3}), ['c'])

    def test_duplicate_keys(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'a': 3}), ['a', 'b'])

    def test_large_input(self):
        test_dict = {str(i): i for i in range(1000)}
        self.assertEqual(get_key(test_dict), list(test_dict.keys()))
