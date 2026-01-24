import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 1)

    def test_single_key_dict(self):
        self.assertEqual(dict_depth({'a': 'b'}), 1)

    def test_nested_dict(self):
        self.assertEqual(dict_depth({'a': {'b': 'c'}}), 2)

    def test_multiple_levels_nested_dict(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 'd'}}}), 3)

    def test_dict_with_non_dict_values(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': {'d': 'e'}}), 2)

    def test_dict_with_non_dict_values_and_empty_dict(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': {'d': 'e'}, 'f': {}}), 2)

    def test_dict_with_non_dict_values_and_multiple_levels_nested_dict(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': {'d': 'e'}, 'f': {'g': {'h': 'i'}}}), 3)

    def test_dict_with_non_dict_values_and_multiple_levels_nested_dict_and_empty_dict(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': {'d': 'e'}, 'f': {'g': {'h': 'i'}, 'j': {}}}), 3)

    def test_dict_with_non_dict_values_and_multiple_levels_nested_dict_and_empty_dict_and_single_key_dict(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': {'d': 'e'}, 'f': {'g': {'h': 'i'}, 'j': {}, 'k': {'l':'m'}}}), 3)
