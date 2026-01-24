import unittest
from mbpp_821_code import ChainMap
from copy import deepcopy

class TestMergeDictionaries(unittest.TestCase):

    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_empty_dict(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict2_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_same_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'b': 4}
        expected = {'a': 3, 'b': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict1_key_not_in_dict2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict2_key_not_in_dict1(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'a': 4}
        expected = {'a': 4, 'b': 2, 'c': 3}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict1_key_overrides_dict2_key(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'b': {'x': 4, 'y': 5}}
        expected = {'a': 1, 'b': {'x': 4, 'y': 5}}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict2_key_overrides_dict1_key(self):
        dict1 = {'a': 1, 'b': {'x': 2, 'y': 3}}
        dict2 = {'a': 3, 'b': 4}
        expected = {'a': 3, 'b': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict1_key_is_list_overrides_dict2_key_is_list(self):
        dict1 = [1, 2]
        dict2 = [3, 4]
        expected = [1, 2, 3, 4]
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict1_key_is_list_overrides_dict2_key_is_not_list(self):
        dict1 = [1, 2]
        dict2 = {'x': 3}
        expected = [1, 2]
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict2_key_is_list_overrides_dict1_key_is_not_list(self):
        dict1 = {'x': 1}
        dict2 = [2, 3]
        expected = [2, 3]
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_dict1_key_is_set_overrides_dict2_key_is_set(self):