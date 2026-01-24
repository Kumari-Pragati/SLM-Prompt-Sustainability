import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        expected = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_same_keys_different_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'c': 4}
        expected = {'a': 3, 'b': 2, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_same_keys_same_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_large_dicts(self):
        dict1 = {str(i): i for i in range(1000)}
        dict2 = {str(i): i for i in range(1000, 2000)}
        expected = {str(i): i for i in range(2000)}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)
