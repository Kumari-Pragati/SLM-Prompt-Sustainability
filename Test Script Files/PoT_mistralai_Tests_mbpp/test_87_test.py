import unittest
from mbpp_87_code import ChainMap
from copy import deepcopy

from87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'c': 5, 'd': 6}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_edge_case_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        dict3 = {'a': 1}
        expected = {'a': 1}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_edge_case_single_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        dict3 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_edge_case_single_key(self):
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        dict3 = {'b': 3}
        expected = {'a': 2}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_corner_case_conflicting_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'b': 4}
        dict3 = {'a': 5, 'b': 6}
        expected = {'a': 5, 'b': 4}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_corner_case_chainmap_order(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'a': 4}
        dict3 = {'c': 5}
        expected = {'a': 4, 'b': 3}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)
