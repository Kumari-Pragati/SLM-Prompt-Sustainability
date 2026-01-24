import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):
    
    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_output = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)
    
    def test_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        expected_output = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)
    
    def test_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected_output = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)
    
    def test_duplicate_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_output = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected_output)
    
    def test_non_dict_inputs(self):
        with self.assertRaises(TypeError):
            merge_dictionaries('not a dict', {'a': 1, 'b': 2})
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1, 'b': 2}, 'not a dict')
        with self.assertRaises(TypeError):
            merge_dictionaries('not a dict', 'not a dict')
