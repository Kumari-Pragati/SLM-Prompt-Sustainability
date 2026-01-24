import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_merge_dictionaries(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_result = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_result)

    def test_merge_dictionaries_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        expected_result = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_result)

    def test_merge_dictionaries_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected_result = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_result)

    def test_merge_dictionaries_same_keys_different_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_result = {'a': 1, 'b': 2, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_result)
