import unittest

from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):
    
    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_output = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)

    def test_edge_case_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        expected_output = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)

    def test_boundary_case_one_empty_dict(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        expected_output = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)

    def test_corner_case_same_keys_different_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_output = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)

    def test_corner_case_same_keys_same_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'b': 2}
        expected_output = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)

    def test_invalid_input_non_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = 'not a dictionary'
        with self.assertRaises(TypeError):
            merge_dictionaries(dict1, dict2)
