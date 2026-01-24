import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(dict_depth({}), 1)
        self.assertEqual(dict_depth({'a': {}}), 2)
        self.assertEqual(dict_depth({'a': {'b': {}}}), 3)
        self.assertEqual(dict_depth({'a': {'b': {'c': {}}}}), 4)

    def test_nested_dicts(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {}}}})), 5)

    def test_empty_values(self):
        self.assertEqual(dict_depth({'a': {}, 'b': {}}), 2)
        self.assertEqual(dict_depth({'a': {'b': {}}, 'c': {}}), 3)

    def test_single_key_dict(self):
        self.assertEqual(dict_depth({'a': {}}), 2)

    def test_non_dict_input(self):
        with self.assertRaises(TypeError):
            dict_depth(123)
        with self.assertRaises(TypeError):
            dict_depth('string')
        with self.assertRaises(TypeError):
            dict_depth([])
