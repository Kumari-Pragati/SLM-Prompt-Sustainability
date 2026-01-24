import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_merge_dictionaries_three(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {'e': 5, 'f': 6}
        result = merge_dictionaries_three(dict1, dict2, dict3)
        self.assertEqual(result, ct.ChainMap({}, dict1, dict2, dict3))
        self.assertEqual(result['a'], 1)
        self.assertEqual(result['b'], 2)
        self.assertEqual(result['c'], 3)
        self.assertEqual(result['d'], 4)
        self.assertEqual(result['e'], 5)
        self.assertEqual(result['f'], 6)

    def test_merge_dictionaries_three_empty(self):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        result = merge_dictionaries_three(dict1, dict2, dict3)
        self.assertEqual(result, ct.ChainMap({}, dict1, dict2, dict3))

    def test_merge_dictionaries_three_dict1_empty(self):
        dict1 = {}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {'e': 5, 'f': 6}
        result = merge_dictionaries_three(dict1, dict2, dict3)
        self.assertEqual(result, ct.ChainMap({}, dict1, dict2, dict3))
        self.assertEqual(result['c'], 3)
        self.assertEqual(result['d'], 4)
        self.assertEqual(result['e'], 5)
        self.assertEqual(result['f'], 6)

    def test_merge_dictionaries_three_dict2_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        dict3 = {'e': 5, 'f': 6}
        result = merge_dictionaries_three(dict1, dict2, dict3)
        self.assertEqual(result, ct.ChainMap({}, dict1, dict2, dict3))
        self.assertEqual(result['a'], 1)
        self.assertEqual(result['b'], 2)
        self.assertEqual(result['e'], 5)
        self.assertEqual(result['f'], 6)

    def test_merge_dictionaries_three_dict3_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        dict3 = {}
        result = merge_dictionaries_three(dict1, dict2, dict3)
        self.assertEqual(result, ct.ChainMap({}, dict1, dict2, dict3))
        self.assertEqual(result['a'], 1)
        self.assertEqual(result['b'], 2)
        self.assertEqual(result['c'], 3)
        self.assertEqual(result['d'], 4)
