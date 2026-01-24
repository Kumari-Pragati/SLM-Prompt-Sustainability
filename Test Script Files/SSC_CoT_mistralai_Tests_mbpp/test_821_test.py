import unittest
from mbpp_821_code import ChainMap
from copy import deepcopy
from 821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_normal_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_edge_case_empty_dicts(self):
        dict1 = {}
        dict2 = {'a': 1}
        expected = {'a': 1}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_edge_case_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_edge_case_dict_keys_conflict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'b': 4}
        expected = {'a': 3, 'b': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_edge_case_dict_values_conflict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'b': 1}
        expected = {'a': 3, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_edge_case_nested_dicts(self):
        dict1 = {'a': {'x': 1}, 'b': 2}
        dict2 = {'a': {'y': 3}, 'c': 4}
        expected = {'a': {'x': 1, 'y': 3}, 'b': 2, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_invalid_input_type_1(self):
        with self.assertRaises(TypeError):
            merge_dictionaries(1, 2)

    def test_invalid_input_type_2(self):
        with self.assertRaises(TypeError):
            merge_dictionaries('a', 'b')

    def test_invalid_input_type_3(self):
        with self.assertRaises(TypeError):
            merge_dictionaries([], {})
