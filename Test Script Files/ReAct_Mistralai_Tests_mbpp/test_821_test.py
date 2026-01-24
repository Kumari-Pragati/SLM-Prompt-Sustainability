import unittest
from mbpp_821_code import ChainMap
from copy import deepcopy
from 821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_empty_dictionaries(self):
        self.assertDictEqual(merge_dictionaries({}, {}), {})

    def test_single_dictionary(self):
        test_dict = {'key1': 'value1'}
        self.assertDictEqual(merge_dictionaries({}, test_dict), test_dict)
        self.assertDictEqual(merge_dictionaries(test_dict, {}), test_dict)

    def test_overlapping_keys(self):
        test_dict1 = {'key1': 'value1', 'key2': 'value2'}
        test_dict2 = {'key1': 'value3', 'key3': 'value4'}
        expected_dict = {'key1': 'value3', 'key2': 'value2', 'key3': 'value4'}
        self.assertDictEqual(merge_dictionaries(test_dict1, test_dict2), expected_dict)

    def test_conflicting_values(self):
        test_dict1 = {'key1': 1, 'key2': 2}
        test_dict2 = {'key1': 3, 'key2': 4}
        expected_dict = {'key1': 3, 'key2': 2}
        self.assertDictEqual(merge_dictionaries(test_dict1, test_dict2), expected_dict)

    def test_deep_merge(self):
        test_dict1 = {'key1': {'key1_1': 'value1'}, 'key2': 2}
        test_dict2 = {'key1': {'key1_2': 'value2'}, 'key3': 3}
        expected_dict = {'key1': {'key1_1': 'value1', 'key1_2': 'value2'}, 'key2': 2, 'key3': 3}
        self.assertDictEqual(merge_dictionaries(deepcopy(test_dict1), deepcopy(test_dict2)), expected_dict)

    def test_key_error(self):
        test_dict1 = {'key1': 'value1'}
        with self.assertRaises(KeyError):
            merge_dictionaries(test_dict1, {'key_not_in_dict1': 'value_not_in_dict1'})
