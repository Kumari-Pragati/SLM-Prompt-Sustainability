import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(dict_depth({}), 0)
        self.assertEqual(dict_depth({'a': 1}), 1)
        self.assertEqual(dict_depth({'a': {'b': 2}}), 2)
        self.assertEqual(dict_depth({'a': {'b': {'c': 3}}}), 3)

    def test_nested_dicts(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': {}}}}), 3)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {}}}})), 4)

    def test_empty_values(self):
        self.assertEqual(dict_depth({'a': {}, 'b': {}}), 1)
        self.assertEqual(dict_depth({'a': {'b': {}}, 'c': {}}), 2)

    def test_non_dict_values(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2}), 1)
        self.assertEqual(dict_depth({'a': {'b': 2}, 'c': 3}), 2)

    def test_mixed_types(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2}}), 2)
        self.assertEqual(dict_depth({'a': {'b': 2}, 'c': {'d': 3}}), 2)
