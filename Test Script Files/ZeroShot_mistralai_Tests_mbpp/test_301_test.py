import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_value_dict(self):
        self.assertEqual(dict_depth({'key': 1}), 1)

    def test_multi_level_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}), 3)

    def test_list_in_dict(self):
        self.assertEqual(dict_depth({'list_val': [1, 2, 3]}), 1)

    def test_tuple_in_dict(self):
        self.assertEqual(dict_depth({'tuple_val': (1, 2, 3)}), 1)

    def test_set_in_dict(self):
        self.assertEqual(dict_depth({'set_val': {1, 2, 3}}), 1)

    def test_none_in_dict(self):
        self.assertEqual(dict_depth({'none_val': None}), 1)

    def test_empty_list_in_dict(self):
        self.assertEqual(dict_depth({'list_val': []}), 1)

    def test_empty_tuple_in_dict(self):
        self.assertEqual(dict_depth({'tuple_val': ()}), 1)

    def test_empty_set_in_dict(self):
        self.assertEqual(dict_depth({'set_val': set()}), 1)
