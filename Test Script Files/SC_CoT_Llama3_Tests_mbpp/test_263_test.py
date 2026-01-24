import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):
    def test_empty_dicts(self):
        d1 = {}
        d2 = {}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {})

    def test_non_empty_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_update_key(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 3})

    def test_update_key_with_same_value(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 2}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_update_key_with_none(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': None}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': None})

    def test_update_key_with_list(self):
        d1 = {'a': 1, 'b': [1, 2]}
        d2 = {'b': [3, 4]}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': [1, 2, 3, 4]})

    def test_update_key_with_dict(self):
        d1 = {'a': 1, 'b': {'x': 1, 'y': 2}}
        d2 = {'b': {'y': 3}}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': {'x': 1, 'y': 3}})

    def test_update_key_with_dict_and_list(self):
        d1 = {'a': 1, 'b': {'x': 1, 'y': [1, 2]}}
        d2 = {'b': {'y': [3, 4]}}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': {'x': 1, 'y': [1, 2, 3, 4]}})
