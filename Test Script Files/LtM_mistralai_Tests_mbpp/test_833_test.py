import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(get_key({'a': 1, 'b': 2, 'c': 3}), ['a', 'b', 'c'])

    def test_empty_input(self):
        self.assertListEqual(get_key({}), [])

    def test_single_input(self):
        self.assertListEqual(get_key({'a': 1}), ['a'])

    def test_key_with_value(self):
        self.assertListEqual(get_key({'a': 1, 'b': 2, 'c': None}), ['a', 'b', 'c'])

    def test_key_with_numeric_value(self):
        self.assertListEqual(get_key({'a': 1, 'b': 2, 'c': 3.14}), ['a', 'b', 'c'])

    def test_key_with_list_value(self):
        self.assertListEqual(get_key({'a': [1, 2, 3], 'b': [4, 5, 6]}), ['a', 'b'])

    def test_key_with_tuple_value(self):
        self.assertListEqual(get_key({'a': (1, 2, 3), 'b': (4, 5, 6)}), ['a', 'b'])
