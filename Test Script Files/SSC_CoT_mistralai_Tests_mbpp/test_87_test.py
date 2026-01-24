import unittest
from mbpp_87_code import ChainMap
from copy import deepcopy
from 87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_typical_input(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'c': 5, 'd': 6}
        expected = {'a': 1, 'b': 3, 'c': 4, 'd': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_edge_cases(self):
        dict1 = deepcopy(self.typical_input_dict)
        del dict1['b']
        self.assertEqual(merge_dictionaries_three(dict1, self.typical_input_dict, self.typical_input_dict), self.typical_input_dict)

        dict2 = deepcopy(self.typical_input_dict)
        dict2['e'] = 7
        self.assertEqual(merge_dictionaries_three(self.typical_input_dict, dict2, self.typical_input_dict), self.typical_input_dict)

        dict3 = deepcopy(self.typical_input_dict)
        del dict3['d']
        self.assertEqual(merge_dictionaries_three(self.typical_input_dict, self.typical_input_dict, dict3), self.typical_input_dict)

    def test_empty_dicts(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})
        self.assertEqual(merge_dictionaries_three({}, {'a': 1}, {}), {'a': 1})
        self.assertEqual(merge_dictionaries_three({'a': 1}, {}, {'a': 2}), {'a': 1})

    def test_chain_map_behavior(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'c': 5, 'd': 6}
        chain_map = ChainMap({}, dict1, dict2, dict3)
        expected = {'a': 1, 'b': 3, 'c': 4, 'd': 6}
        self.assertEqual(dict(chain_map), expected)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            merge_dictionaries_three(1, 2, 3)
        with self.assertRaises(TypeError):
            merge_dictionaries_three([], {}, {})
        with self.assertRaises(TypeError):
            merge_dictionaries_three({}, 2, {})
        with self.assertRaises(TypeError):
            merge_dictionaries_three({}, {}, 2)
