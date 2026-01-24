import unittest
from mbpp_263_code import deepcopy
from 263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_empty_dict(self):
        d1 = {}
        d2 = {}
        result = merge_dict(d1, d2)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, d1)

    def test_one_element_dict(self):
        d1 = {'a': 1}
        d2 = {'b': 2}
        result = merge_dict(d1, d2)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_overwrite_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'c': 4}
        result = merge_dict(d1, d2)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'a': 3, 'b': 2, 'c': 4})

    def test_deep_merge(self):
        d1 = {'a': 1, 'b': {'x': 1, 'y': 2}}
        d2 = {'a': 3, 'b': {'y': 4, 'z': 5}}
        result = merge_dict(d1, d2)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'a': 3, 'b': {'x': 1, 'y': 4, 'z': 5}})

    def test_copy_functionality(self):
        d1 = {'a': 1, 'b': {'x': 1, 'y': 2}}
        d2 = merge_dict(d1, {})
        self.assertIsInstance(d2, dict)
        self.assertNotEqual(d1, d2)
        self.assertEqual(d1, d1)
        self.assertEqual(d2, d2)
