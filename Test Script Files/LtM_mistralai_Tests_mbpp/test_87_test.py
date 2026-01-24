import unittest
from mbpp_87_code import ChainMap
from copy import deepcopy
from 87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_simple_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'c': 5, 'd': 6}
        expected = {'a': 1, 'b': 3, 'c': 4, 'd': 6}
        self.assertDictEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_empty_dicts(self):
        self.assertDictEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_dict_with_empty_dicts(self):
        dict1 = {'a': 1, 'b': 2}
        self.assertDictEqual(merge_dictionaries_three(dict1, {}, {}), dict1)
        self.assertDictEqual(merge_dictionaries_three({}, dict1, {}), dict1)
        self.assertDictEqual(merge_dictionaries_three({}, {}, dict1), {})

    def test_dict_with_chain_map(self):
        dict1 = {'a': 1, 'b': 2}
        chain_map = ChainMap({'b': 3}, dict1)
        expected = {'a': 1, 'b': 3}
        self.assertDictEqual(merge_dictionaries_three({}, {}, chain_map), expected)

    def test_chain_map_with_dict(self):
        dict1 = {'a': 1, 'b': 2}
        chain_map = ChainMap({'b': 3}, {'c': 4})
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertDictEqual(merge_dictionaries_three(dict1, {}, chain_map), expected)

    def test_chain_map_with_dict_with_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        chain_map = ChainMap({'b': 3}, {'c': 4}, {})
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertDictEqual(merge_dictionaries_three(dict1, {}, chain_map), expected)
