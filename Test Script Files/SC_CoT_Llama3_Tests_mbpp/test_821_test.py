import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_typical_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, ct.ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {}))

    def test_merge_with_overlapping_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, ct.ChainMap({'a': 1, 'b': 3}, {'c': 4}, {}))

    def test_merge_with_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, ct.ChainMap({}, {}))

    def test_merge_with_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, ct.ChainMap({'a': 1, 'b': 2}, {}))

    def test_merge_with_one_dict(self):
        dict1 = {}
        dict2 = {'c': 3, 'd': 4}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, ct.ChainMap({}, {'c': 3, 'd': 4}))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            merge_dictionaries(123, {'a': 1, 'b': 2})

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1, 'b': 2},'string')
