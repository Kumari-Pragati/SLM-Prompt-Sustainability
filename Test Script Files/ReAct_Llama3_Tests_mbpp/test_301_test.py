import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 1)

    def test_single_key_dict(self):
        self.assertEqual(dict_depth({'a': 'b'}), 1)

    def test_nested_dict(self):
        self.assertEqual(dict_depth({'a': {'b': 'c'}}), 2)

    def test_multiple_levels(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 'd'}}}), 3)

    def test_dict_with_non_dict_values(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': 1}), 1)

    def test_dict_with_non_dict_values_and_nested_dict(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': {'d': 'e'}}), 2)

    def test_dict_with_empty_list(self):
        self.assertEqual(dict_depth({'a': []}), 1)

    def test_dict_with_empty_tuple(self):
        self.assertEqual(dict_depth({'a': ()}), 1)

    def test_dict_with_non_dict_values_and_empty_list(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': []}), 1)

    def test_dict_with_non_dict_values_and_empty_tuple(self):
        self.assertEqual(dict_depth({'a': 'b', 'c': ()}), 1)
