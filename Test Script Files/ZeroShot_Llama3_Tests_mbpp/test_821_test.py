import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_empty_dictionaries(self):
        dict1 = {}
        dict2 = {}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, {})

    def test_non_empty_dictionaries(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})

    def test_dict1_is_empty_dict2_is_non_empty(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_dict2_is_empty_dict1_is_non_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_dict1_and_dict2_are_non_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})
