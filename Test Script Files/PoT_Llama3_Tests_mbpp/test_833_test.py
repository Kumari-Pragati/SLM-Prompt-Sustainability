import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'c': 3}), ['a', 'b', 'c'])

    def test_empty_dict(self):
        self.assertEqual(get_key({}), [])

    def test_single_key_dict(self):
        self.assertEqual(get_key({'a': 1}), ['a'])

    def test_multiple_key_dict(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'c': 3, 'd': 4}), ['a', 'b', 'c', 'd'])

    def test_dict_with_duplicates(self):
        self.assertEqual(get_key({'a': 1, 'a': 2, 'b': 3, 'c': 4}), ['a', 'a', 'b', 'c'])

    def test_dict_with_non_string_keys(self):
        with self.assertRaises(TypeError):
            get_key({1: 2, 3: 4})
