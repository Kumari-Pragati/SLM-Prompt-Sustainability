import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_simple_dict(self):
        self.assertEqual(dict_depth({'a': 1}), 1)

    def test_nested_dict(self):
        self.assertEqual(dict_depth({'a': {'b': 1}}), 2)

    def test_nested_dict_with_empty_value(self):
        self.assertEqual(dict_depth({'a': {'b': {}}}), 2)

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_dict_with_multiple_levels(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 1}}}), 3)

    def test_dict_with_multiple_levels_and_empty_values(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': {}}}}), 3)

    def test_dict_with_multiple_levels_and_mixed_types(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 1, 'd': []}}}), 3)

    def test_dict_with_multiple_levels_and_mixed_types_and_empty_values(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 1, 'd': []}, 'e': {}}}), 3)
