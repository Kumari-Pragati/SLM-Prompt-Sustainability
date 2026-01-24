import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_typical_inputs(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {'e': 5, 'f': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

    def test_edge_case_empty_dict(self):
        dict1 = {}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {'e': 5, 'f': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), {'c': 3, 'd': 4, 'e': 5, 'f': 6})

    def test_edge_case_single_dict(self):
        dict1 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries_three(dict1, {}, {}), {'a': 1, 'b': 2})

    def test_edge_case_empty_dict1(self):
        dict1 = {}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), {'c': 3, 'd': 4})

    def test_edge_case_empty_dict2(self):
        dict1 = {}
        dict2 = {}
        dict3 = {'e': 5, 'f': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), {'e': 5, 'f': 6})

    def test_edge_case_empty_dict3(self):
        dict1 = {}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), {'c': 3, 'd': 4})

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            merge_dictionaries_three(123, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            merge_dictionaries_three({'a': 1, 'b': 2}, 'hello', {'e': 5, 'f': 6})

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            merge_dictionaries_three({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, 'world')
