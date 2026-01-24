import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_level_dict(self):
        self.assertEqual(dict_depth({'a': 1}), 1)

    def test_two_level_dict(self):
        self.assertEqual(dict_depth({'a': {'b': 2}}), 2)

    def test_three_level_dict(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': 3}}}), 3)

    def test_dict_with_non_dict_values(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2}}), 2)

    def test_dict_with_non_dict_values_and_empty_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2, 'd': {}}}), 2)

    def test_dict_with_non_dict_values_and_multiple_levels(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}), 3)
