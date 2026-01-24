import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_edge_case_empty_dict1(self):
        dict1 = {}
        dict2 = {'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'c': 3, 'd': 4})

    def test_edge_case_empty_dict2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'a': 1, 'b': 2})

    def test_edge_case_dict1_is_dict2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'a': 1, 'b': 2})

    def test_edge_case_dict1_is_empty_dict2_is_empty(self):
        dict1 = {}
        dict2 = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), {})

    def test_edge_case_dict1_is_empty_dict2_is_not_empty(self):
        dict1 = {}
        dict2 = {'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'c': 3, 'd': 4})

    def test_edge_case_dict1_is_not_empty_dict2_is_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'a': 1, 'b': 2})

    def test_edge_case_dict1_is_not_empty_dict2_is_not_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'a': 1, 'b': 2, 'c': 3, 'd': 4})
