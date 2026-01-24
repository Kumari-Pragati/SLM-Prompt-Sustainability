import unittest
from mbpp_821_code import ChainMap
from copy import deepcopy

from821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_simple_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_empty_merge(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_conflicting_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'b': 4}
        expected = {'a': 3, 'b': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_chainmap_behavior(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = ChainMap({'a': 1, 'b': 2}, dict1, dict2)
        self.assertEqual(merge_dictionaries(dict1, dict2), dict(expected))

    def test_deep_merge(self):
        dict1 = {'a': 1, 'b': {'x': 2, 'y': 3}}
        dict2 = {'b': {'x': 4, 'z': 5}, 'c': 6}
        expected = {'a': 1, 'b': {'x': 4, 'y': 3, 'z': 5}, 'c': 6}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)
