import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_simple_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_empty_dict1(self):
        dict1 = {}
        dict2 = {'b': 3, 'c': 4}
        expected = {'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_empty_dict2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        expected = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_same_keys_different_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'b': 4}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_same_keys_same_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)
