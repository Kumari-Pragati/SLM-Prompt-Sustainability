import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_level_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2}), 1)

    def test_two_level_dict(self):
        self.assertEqual(dict_depth({'a': {'x': 1, 'y': 2}, 'b': 3}), 2)

    def test_three_level_dict(self):
        self.assertEqual(dict_depth({'a': {'x': 1, 'y': {'z': 3, 'w': 4}}, 'b': 5}), 3)

    def test_dict_with_non_dict_values(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': {'x': 3, 'y': 4}}), 1)

    def test_dict_with_non_dict_values_and_empty_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': {'x': 3, 'y': 4, 'd': {}}}), 2)

    def test_dict_with_non_dict_values_and_non_empty_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': 2, 'c': {'x': 3, 'y': 4, 'd': {'e': 5}}}), 3)
