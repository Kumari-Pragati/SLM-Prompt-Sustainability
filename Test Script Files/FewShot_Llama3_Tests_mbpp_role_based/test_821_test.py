import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):
    def test_empty_dictionaries(self):
        dict1 = {}
        dict2 = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), {})

    def test_single_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), dict1)

    def test_multiple_dicts(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {'e': 5, 'f': 6}
        self.assertEqual(merge_dictionaries(dict1, dict2, dict3), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

    def test_conflicting_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'a': 1, 'b': 2, 'c': 4})

    def test_non_dict_input(self):
        with self.assertRaises(TypeError):
            merge_dictionaries('not a dict', {})
